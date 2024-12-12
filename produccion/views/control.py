from django.shortcuts import render, redirect, get_object_or_404
from produccion.models import Produccion, PostProduccion
from produccion.forms import PostProduccionForm
from datetime import date

def control_produccion(request, context):
    # Obtener datos
    producciones = Produccion.objects.all()

    # Formularios
    #produccion_form = ProduccionForm(request.POST or None)

    # Procesar formularios
    if request.method == 'POST':
        if "mandar_a_venta" in request.POST:
            return mandar_a_venta(request)
        
        if "eliminar_produccion" in request.POST:
            return eliminar_produccion(request)

    # Actualizar el contexto y renderizar
    context.update({
        'producciones': producciones,
        #'produccion_form': produccion_form,
    })

    return render(request, 'produccion/manager.html', context)

def mandar_a_venta(request):
    # Obtener cálculo relacionado
    produccion_id = request.POST.get("produccion_id")
    produccion = get_object_or_404(Produccion, id=produccion_id)

    # Procesar formulario de Producción
    form = PostProduccionForm(request.POST)
    if form.is_valid():
        postProduccion = form.save(commit=False)
        # Llenar datos de cálculo en el modelo de Producción
        postProduccion.fecha = date.today()
        postProduccion.producto = produccion.producto
        postProduccion.filamento = produccion.filamento
        postProduccion.cantidad  = produccion.cantidad
        postProduccion.peso = produccion.peso
        postProduccion.costo = produccion.costo
        postProduccion.save()
        
        # Eliminar cálculo una vez procesado
        #produccion.delete()
        
        return redirect('/manager/?screen=venta')

def eliminar_produccion(request):
    produccion_id = request.POST.get("produccion_id")
    produccion = get_object_or_404(Produccion, id=produccion_id)
    produccion.delete()
    return redirect('/manager/?screen=control_produccion')
