from django import forms
from dal import autocomplete
from apl_euphoria.models import Cliente,CategoriaProducto, MarcaCosmetico, Producto

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
    
