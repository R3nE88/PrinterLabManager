from django.shortcuts import render
from .gestion import gestionar_materiales
from .calculadora import calculadora_produccion
from .control import control_produccion
from .venta import venta

# Vista principal del manager
def manager(request):
    screen = request.GET.get('screen', 'calculadora_produccion')  # Pantalla actual
    context = {'screen': screen}

    # Delegar el manejo de cada pantalla
    if screen == "gestion_materiales":
        return gestionar_materiales(request, context)
    
    if screen == "control_produccion":
        return control_produccion(request, context)

    if screen == "calculadora_produccion":
        return calculadora_produccion(request, context)
    
    if screen == "venta":
        return venta(request, context)

    # Pantalla por defecto
    return render(request, 'produccion/manager.html', context)
