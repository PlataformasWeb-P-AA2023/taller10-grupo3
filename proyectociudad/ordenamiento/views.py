from django.shortcuts import render, redirect

from ordenamiento.models import *
from ordenamiento.forms import *


def home(request):
    return redirect('admin:index')


def index(request):
    parroquias = Parroquia.objects.all()
    displayed_data = {'parroquias': parroquias}

    return render(request, 'index.html', displayed_data)


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

def editar_barrio(request, id):
    barrio = Barrio.objects.get(pk=id)
    if request.method == 'POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm(instance=barrio)
    form = {'title': "Editar Barrio", 'formulario': formulario}

    return render(request, 'edit_createSkeleton.html', form)