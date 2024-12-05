from django.shortcuts import render, redirect, get_object_or_404
from produccion.models import Calculo
from produccion.forms import CalculoForm

'''
def calculadora_produccion(request, context):
    # Obtener datos
    calculadora = Calculo.objects.all()

    # Formularios
    calculo_form = CalculoForm(request.POST or None)

    #procesar formulario
    if request.method == "POST":
        if "editar_calculo" in request.POST:
            calculo_id = request.POST.get("calculo_id")
            calculo = get_object_or_404(Calculo, id=calculo_id)

            calculo_form = CalculoForm(request.POST, instance=calculo)
            if calculo_form.is_valid():
                calculo_form.save()
                return redirect('/manager/?screen=calculadora_produccion')
            
        if "nuevo_calculo" in request.POST and calculo_form.is_valid():
            try:
                calculo_form.save()
            except Exception as e:
                print(f"Error al guardar: {e}")
            
            print(request.POST)
            return redirect('/manager/?screen=calculadora_produccion')

        if "eliminar_calculo" in request.POST:
            return eliminar_calculo(request)

    # Actualizar el contexto y renderizar
    context.update({
        'calculadora': calculadora,
        'calculo_form': calculo_form,
    })
    
    return render(request, 'produccion/manager.html', context)

def eliminar_calculo(request):
    calculo_id = request.POST.get("calculo_id")
    calculo = get_object_or_404(calculo, id=calculo_id)
    calculo.delete()
    return redirect('/manager/?screen=calculadora_produccion')
    '''


def calculadora_produccion(request, context):
    if request.method == 'POST':
        form = CalculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/manager/?screen=calculadora_produccion')  # Redirige a la misma página tras guardar
    else:
        form = CalculoForm()

    calculos = Calculo.objects.all()  # Obtén todos los cálculos para la tabla

    # Actualizar el contexto y renderizar
    context.update({
        'calculadora': calculos,
        'calculo_form': form,
    })

    return render(request, 'produccion/manager.html', context)
    