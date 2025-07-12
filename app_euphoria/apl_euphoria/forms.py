from django import forms
from apl_euphoria.models import Cliente
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
    
