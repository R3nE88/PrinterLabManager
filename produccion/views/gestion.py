from django.shortcuts import render, redirect, get_object_or_404
from produccion.models import Filamento, Material
from produccion.forms import FilamentoForm, MaterialForm

# gestionar materiales y filamentos
def gestionar_materiales(request, context):
    # Obtener datos de Filamentos y Materiales
    filamentos = Filamento.objects.all()
    materiales = Material.objects.all()

    # Formularios
    filamento_form = FilamentoForm(request.POST or None)
    material_form = MaterialForm(request.POST or None)

    # Procesar formularios de agregar/editar
    if request.method == "POST":
        if "editar_filamento" in request.POST:
            return editar_filamento(request)

        if "nuevo_filamento" in request.POST and filamento_form.is_valid():
            filamento_form.save()
            return redirect('/manager/?screen=gestion_materiales')

        if "editar_material" in request.POST:
            return editar_material(request)

        if "nuevo_material" in request.POST and material_form.is_valid():
            material_form.save()
            return redirect('/manager/?screen=gestion_materiales')

        if "eliminar_filamento" in request.POST:
            return eliminar_filamento(request)

        if "eliminar_material" in request.POST:
            return eliminar_material(request)

    # Actualizar el contexto y renderizar
    context.update({
        'filamentos': filamentos,
        'materiales': materiales,
        'filamento_form': filamento_form,
        'material_form': material_form,
    })
    return render(request, 'produccion/manager.html', context)

def editar_filamento(request):
    filamento_id = request.POST.get("filamento_id")
    filamento = get_object_or_404(Filamento, id=filamento_id)

    filamento_form = FilamentoForm(request.POST, instance=filamento)
    if filamento_form.is_valid():
        filamento_form.save()
        return redirect('/manager/?screen=gestion_materiales')

def eliminar_filamento(request):
    filamento_id = request.POST.get("filamento_id")
    filamento = get_object_or_404(Filamento, id=filamento_id)
    filamento.delete()
    return redirect('/manager/?screen=gestion_materiales')

def editar_material(request):
    material_id = request.POST.get("material_id")
    material = get_object_or_404(Material, id=material_id)

    material_form = MaterialForm(request.POST, instance=material)
    if material_form.is_valid():
        material_form.save()
        return redirect('/manager/?screen=gestion_materiales')

def eliminar_material(request):
    material_id = request.POST.get("material_id")
    material = get_object_or_404(Material, id=material_id)
    material.delete()
    return redirect('/manager/?screen=gestion_materiales')