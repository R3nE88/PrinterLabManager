from django.shortcuts import render, redirect, get_object_or_404
from produccion.models import Produccion
from produccion.forms import ProduccionForm

def control_produccion(request, context):
    # Obtener datos
    producciones = Produccion.objects.all()

    # Formularios
    produccion_form = ProduccionForm(request.POST or None)

    # Procesar formularios
    if request.method == 'POST':
        if "nueva_produccion" in request.POST and produccion_form.is_valid():
            produccion_form.save()
            return redirect('/manager/?screen=control_produccion')

        if "editar_produccion" in request.POST:
            return editar_produccion(request)
        
        if "eliminar_produccion" in request.POST:
            return eliminar_produccion(request)

    # Actualizar el contexto y renderizar
    context.update({
        'producciones': producciones,
        'produccion_form': produccion_form,
    })

    return render(request, 'produccion/manager.html', context)


def editar_produccion(request):
    print(request.body)
    produccion_id = request.POST.get("produccion_id")
    produccion = get_object_or_404(Produccion, id=produccion_id)

    produccion_form = ProduccionForm(request.POST, instance=produccion)
    if produccion_form.is_valid():
        produccion_form.save()
        return redirect('/manager/?screen=control_produccion')

def eliminar_produccion(request):
    produccion_id = request.POST.get("produccion_id")
    produccion = get_object_or_404(Produccion, id=produccion_id)
    produccion.delete()
    return redirect('/manager/?screen=control_produccion')
