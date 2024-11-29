from django.shortcuts import render
from .gestion import gestionar_materiales
from .calculadora import calculadora_produccion

# Vista principal del manager
def manager(request):
    screen = request.GET.get('screen', 'calculadora_produccion')  # Pantalla actual
    context = {'screen': screen}

    # Delegar el manejo de cada pantalla
    if screen == "gestion_materiales":
        return gestionar_materiales(request, context)

    # Otras pantallas
    if screen == "calculadora_produccion":
        return calculadora_produccion(request, context)

    # Pantalla por defecto
    return render(request, 'produccion/manager.html', context)
