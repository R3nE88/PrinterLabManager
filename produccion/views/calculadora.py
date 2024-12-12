from django.shortcuts import render, redirect, get_object_or_404
from produccion.models import Calculo, Filamento
from produccion.forms import CalculoForm, CalculoFormEdit, ProduccionForm
from datetime import date

def calculadora_produccion(request, context):
    # Obtener datos
    calculos = Calculo.objects.all()
    filamentos = Filamento.objects.all()

    # Formularios
    calculo_form = CalculoForm(request.POST or None)

    # Procesar formularios
    if request.method == 'POST':
        if "recalcular" in request.POST:
            return recalcular(request)

        if "nuevo_calculo" in request.POST and calculo_form.is_valid():
            calculo_form.save()
            return redirect('/manager/?screen=calculadora_produccion')

        if "editar_calculo" in request.POST:
            return editar_calculo(request)
        
        if "eliminar_calculo" in request.POST:
            return eliminar_calculo(request)
        
        if "mandar_a_produccion" in request.POST:
            return mandar_a_produccion(request)

    # Actualizar el contexto y renderizar
    context.update({
        'calculadora': calculos,
        'calculo_form': calculo_form,
        'filamentos': filamentos,
    })

    return render(request, 'produccion/manager.html', context)
    
def mandar_a_produccion(request):
    # Obtener cálculo relacionado
    calculo_id = request.POST.get("calculo_id")
    calculo = get_object_or_404(Calculo, id=calculo_id)
    
    # Procesar formulario de Producción
    form = ProduccionForm(request.POST)
    if form.is_valid():
        produccion = form.save(commit=False)
        # Llenar datos de cálculo en el modelo de Producción
        produccion.fecha = date.today()
        produccion.producto = calculo.producto
        produccion.filamento = calculo.filamento
        produccion.peso = calculo.peso
        produccion.tiempo = calculo.tiempo
        produccion.costo = calculo.costo
        produccion.save()
        
        # Eliminar cálculo una vez procesado
        calculo.delete()
        
        return redirect('/manager/?screen=control_produccion')

def recalcular(request):
    calculo_id = request.POST.get("calculo_id")
    calculo = get_object_or_404(Calculo, id=calculo_id)

    calculo_form = CalculoFormEdit(request.POST, instance=calculo)
    if calculo_form.is_valid():
        calculo_form.save()
        return redirect('/manager/?screen=calculadora_produccion')

def editar_calculo(request):
    print(request.body)
    calculo_id = request.POST.get("calculo_id")
    calculo = get_object_or_404(Calculo, id=calculo_id)

    calculo_form = CalculoFormEdit(request.POST, instance=calculo)
    if calculo_form.is_valid():
        calculo_form.save()
        return redirect('/manager/?screen=calculadora_produccion')

def eliminar_calculo(request):
    calculo_id = request.POST.get("calculo_id")
    calculo = get_object_or_404(Calculo, id=calculo_id)
    calculo.delete()
    return redirect('/manager/?screen=calculadora_produccion')
