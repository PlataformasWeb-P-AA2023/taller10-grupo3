from django.shortcuts import render, redirect

from ordenamiento.models import *
from ordenamiento.forms import *

#redirige al usuario a la interfaz de administración por la función de redirección de admin:index.
def home(request):
    return redirect('admin:index')


def index(request):
    parroquias = Parroquia.objects.all()
    displayed_data = {'parroquias': parroquias}

    return render(request, 'index.html', displayed_data)

#crear, si el método de solicitud es 'POST'.
def crear_parroquia(request):
    if request.method == 'POST':
        formulario = ParroquiaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()

    form = {'title': "Editar Parroquia", 'formulario': formulario}

    return render(request, 'edit_createSkeleton.html', form)

#La función de vista editar_parroquia maneja la edición de un objeto Parroquia 
def editar_parroquia(request, id):
    parroquia = Parroquia.objects.get(pk=id)
    if request.method == 'POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    form = {'title': "Editar Parroquia", 'formulario': formulario}

    return render(request, 'edit_createSkeleton.html', form)

#La función de vista crear_barrio maneja la creación de un nuevo objeto Barrio.
def crear_barrio(request):
    if request.method == 'POST':
        formulario = BarrioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm()

    form = {'title': "Crear Barrio", 'formulario': formulario}

    return render(request, 'edit_createSkeleton.html', form)

#La función de vista editar_barrio maneja la edición de un objeto Barrio 
#manejan las diferentes acciones como la representación de plantillas, el manejo de envíos de formularios 

def editar_barrio(request, id):
    barrio = Barrio.objects.get(pk=id)
    if request.method == 'POST':
        formulario = BarrioEditForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioEditForm(instance=barrio)
    form = {'title': "Editar Barrio", 'formulario': formulario}

    return render(request, 'edit_createSkeleton.html', form)