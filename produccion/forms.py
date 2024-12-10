from django import forms
from .models import Filamento, Material, Calculo, Produccion
from datetime import date

class FilamentoForm(forms.ModelForm):
    class Meta:
        model = Filamento
        fields = ['marca', 'tipo', 'cantidad', 'color', 'restante', 'valor']
        labels = {
            'marca': 'Marca',
            'tipo': 'Tipo de filamento',
            'cantidad': 'Unidades',
            'color': 'Color',
            'restante': 'Restante(gramos)',
            'valor': 'Valor en dolar'
        }

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['material', 'valor']
        labels = {
            'material': 'Material',
            'valor': 'Valor en pesos'
        }

class CalculoFormEdit(forms.ModelForm): #no recalcula la fecha
    class Meta:
        model = Calculo
        fields = ['producto', 'filamento', 'peso', 'tiempo', 'fecha']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['filamento'].queryset = Filamento.objects.all()

    def save(self, commit=True):
        instance = super().save(commit=False)
        filamento = self.cleaned_data['filamento']
        instance.costo = round(filamento.valor / 1000 * self.cleaned_data['peso'], 2)
        if commit:
            instance.save()
        return instance
       
class CalculoForm(forms.ModelForm):
    class Meta:
        model = Calculo
        fields = ['producto', 'filamento', 'peso', 'tiempo']
        labels = {
            'peso': 'Peso (gramos):',  # Cambia el texto de la etiqueta
            'producto': 'Nombre del Producto:',
            'filamento': 'Tipo de Filamento:',
            'tiempo': 'Tiempo de Impresión (Minutos):',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['filamento'].queryset = Filamento.objects.all()

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.fecha = date.today()  # Asigna la fecha actual
        filamento = self.cleaned_data['filamento']
        instance.costo = round(filamento.valor / 1000 * self.cleaned_data['peso'], 2)
        if commit:
            instance.save()
        return instance

#class MandarAProduccionForm(forms.modelForm):

 
class ProduccionForm(forms.ModelForm):
    class Meta:
        model = Produccion
        fields = ['cantidad', 'valor']

    def save(self, commit=True):
        instance = super().save(commit=False)
        print(instance.valor)
        print(instance.valor / 20.30)
        instance.valor = round(instance.valor / 20.30, 5)
        if commit:
            instance.save()
        return instance
    
    #PRECIO DEL DOLAR AQUI