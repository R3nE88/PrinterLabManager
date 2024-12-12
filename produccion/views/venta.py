from django.shortcuts import render, redirect, get_object_or_404
from produccion.models import PostProduccion

def venta(request, context):
    # Obtener datos
    postProduccion = PostProduccion.objects.all()

    # Procesar formularios
    if request.method == 'POST':
        print(postProduccion)
        if "eliminar_postproduccion" in request.POST:
            return eliminar_produccion(request)

    # Actualizar el contexto y renderizar
    context.update({
        'postproducciones': postProduccion,
    })

    return render(request, 'produccion/manager.html', context)


def eliminar_produccion(request):
    produccion_id = request.POST.get("postproduccion_id")
    produccion = get_object_or_404(PostProduccion, id=produccion_id)
    produccion.delete()
    return redirect('/manager/?screen=venta')
