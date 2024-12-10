from django.shortcuts import render, redirect, get_object_or_404
from produccion.models import Calculo, Filamento
from produccion.forms import CalculoForm

def calculadora_produccion(request, context):
    # Obtener datos
    calculos = Calculo.objects.all()
    filamentos = Filamento.objects.all()

    # Formularios
    calculo_form = CalculoForm(request.POST or None)

    # Procesar formularios
    if request.method == 'POST':
        if "nuevo_calculo" in request.POST and calculo_form.is_valid():
            calculo_form.save()
            return redirect('/manager/?screen=calculadora_produccion')

        if "editar_calculo" in request.POST:
            return editar_calculo(request)
        
        if "eliminar_calculo" in request.POST:
            return eliminar_calculo(request)

    # Actualizar el contexto y renderizar
    context.update({
        'calculadora': calculos,
        'calculo_form': calculo_form,
        'filamentos': filamentos,
    })

    return render(request, 'produccion/manager.html', context)

def editar_calculo(request):
    calculo_id = request.POST.get("calculo_id")
    calculo = get_object_or_404(Calculo, id=calculo_id)

    calculo_form = CalculoForm(request.POST, instance=calculo)
    if calculo_form.is_valid():
        calculo_form.save()
        return redirect('/manager/?screen=calculadora_produccion')

def eliminar_calculo(request):
    calculo_id = request.POST.get("calculo_id")
    calculo = get_object_or_404(Calculo, id=calculo_id)
    calculo.delete()
    return redirect('/manager/?screen=calculadora_produccion')
