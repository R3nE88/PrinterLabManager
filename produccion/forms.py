from django import forms
from .models import Filamento, Material, CalculadoraProduccion

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
        model = CalculadoraProduccion
        fields = ['fecha', 'producto', 'filamento', 'peso', 'tiempo', 'costo']