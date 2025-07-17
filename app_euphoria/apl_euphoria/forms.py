from django import forms
from dal import autocomplete
from apl_euphoria.models import Cliente,CategoriaProducto, MarcaCosmetico, Producto, Pedido, DetallePedido, Venta

class ClienteForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100, required=True)
    apellido = forms.CharField(label='Apellido', max_length=100, required=True)
    email = forms.EmailField(label='Email', required=True)
    telefono = forms.CharField(label='Teléfono', max_length=15, required=False)
   

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("El campo Email es obligatorio.")
        return email
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono and not telefono.isdigit():
            raise forms.ValidationError("El campo Teléfono debe contener solo números.")
        return telefono
    def save(self):
        cliente = Cliente(
            nombre=self.cleaned_data['nombre'],
            apellido=self.cleaned_data['apellido'],
            email=self.cleaned_data['email'],
            telefono=self.cleaned_data.get('telefono', ''),
            direccion=self.cleaned_data.get('direccion', '')
        )
        cliente.save()
        return cliente
    
#  Formulario para crear o editar una categoría de producto
class CategoriaProductoForm(forms.ModelForm):
    class Meta:
        model = CategoriaProducto
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError("El campo Nombre es obligatorio.")
        return nombre
    
# formulario de marca  para crear o editar una marca de cosmético
class MarcaCosmeticoForm(forms.ModelForm):
    class Meta:
        model = MarcaCosmetico
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError("El campo Nombre es obligatorio.")
        return nombre
    
# Formulario para crear o editar un producto  
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock', 'categoria', 'marca']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': autocomplete.ModelSelect2(
                url='apl_euphoria:categoria-autocomplete',  # Agrega el namespace
                attrs={'class': 'form-control'}
            ),
            'marca': autocomplete.ModelSelect2(
                url='apl_euphoria:marca-autocomplete',  # Agrega el namespace
                attrs={'class': 'form-control'}
            ),
        }
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError("El campo Nombre es obligatorio.")
        return nombre
    
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['id_cliente', 'fecha']
        widgets = {
            'id_cliente': autocomplete.ModelSelect2(
                url='apl_euphoria:cliente-autocomplete',  # Agrega el namespace
                attrs={'class': 'form-control'}
            ),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
    
    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if not fecha:
            raise forms.ValidationError("El campo Fecha es obligatorio.")
        return fecha
class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = ['id_pedido', 'id_producto', 'cantidad']
        widgets = {
            'id_pedido': autocomplete.ModelSelect2(
                url='apl_euphoria:pedido-autocomplete',  # Agrega el namespace
                attrs={'class': 'form-control'}
            ),
            'id_producto': autocomplete.ModelSelect2(
                url='apl_euphoria:producto-autocomplete',  # Agrega el namespace
                attrs={'class': 'form-control'}
            ),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad <= 0:
            raise forms.ValidationError("La cantidad debe ser mayor que cero.")
        return cantidad
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['id_vendedor', 'detalles', 'total', 'subtotal', 'fecha', 'cantidad', 'id_administrador', 'id_pedido', 'id_producto']
        widgets = {
            'id_vendedor': autocomplete.ModelSelect2(
                url='apl_euphoria:vendedor-autocomplete',  # Agrega el namespace
                attrs={'class': 'form-control'}
            ),
            
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
            'subtotal': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_administrador': autocomplete.ModelSelect2(
                url='apl_euphoria:administrador-autocomplete',  # Agrega el namespace
                attrs={'class': 'form-control'}
            ),
            'id_pedido': autocomplete.ModelSelect2(
                url='apl_euphoria:pedido-autocomplete',  # Agrega el namespace
                attrs={'class': 'form-control'}
            ),
            'id_producto': autocomplete.ModelSelect2(
                url='apl_euphoria:producto-autocomplete',  # Agrega el namespace
                attrs={'class': 'form-control'}
            ),
            'detalles': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    
    def clean_total(self):
        total = self.cleaned_data.get('total')
        if total <= 0:
            raise forms.ValidationError("El total debe ser mayor que cero.")
        return total