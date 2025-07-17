from django import forms
from django.forms import ModelForm
from apl_euphoria.models import Pago, Factura

class PagoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Establecer autofocus en el campo nombre
        self.fields['nombre'].widget.attrs['autofocus'] = True
        
        # Opcional: Aplicar estilos comunes a todos los campos
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
            field.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Pago
        fields = '__all__'  # Corregido: sin corchetes para '__all__'
        
    class FacturaForm(forms.ModelForm):
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Establecer autofocus en el campo nombre
        self.fields['nombre'].widget.attrs['autofocus'] = True
        
        # Opcional: Aplicar estilos comunes a todos los campos
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
            field.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Factura
        fields = '__all__'  # Corregido: sin corchetes para '__all__'