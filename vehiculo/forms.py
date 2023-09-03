from django import forms
from .models import Vehiculo

class AddVehiculo(forms.ModelForm):
    class Meta:
        model = Vehiculo
        exclude = ['fecha_de_modificacion', 'fecha_de_creacion']