from django.shortcuts import render, redirect, get_object_or_404
from produccion.models import CalculadoraProduccion
from produccion.forms import CalculoForm

def calculadora_produccion(request, context):
    # Obtener datos
    calculadora = CalculadoraProduccion.objects.all()

    # Formularios
    filamento_form = CalculoForm(request.POST or None)

    return render(request, 'produccion/manager.html', context)