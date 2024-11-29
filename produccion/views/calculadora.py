from django.shortcuts import render, redirect, get_object_or_404
from produccion.models import CalculadoraProduccion

def calculadora_produccion(request, context):
    calculadora = CalculadoraProduccion.objects.all()
    return render(request, 'produccion/manager.html', context)