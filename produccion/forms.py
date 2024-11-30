from django import forms
from .models import Filamento, Material, Calculo

class FilamentoForm(forms.ModelForm):
    class Meta:
        model = Filamento
        fields = ['marca', 'tipo', 'cantidad', 'color', 'restante', 'valor']

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['material', 'valor']

class CalculoForm(forms.ModelForm):
    class Meta:
        model = Calculo
        fields = ['fecha', 'producto', 'filamento', 'peso', 'tiempo', 'costo']