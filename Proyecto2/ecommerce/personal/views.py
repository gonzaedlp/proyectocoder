from django.shortcuts import render, redirect
from personal.models import Personal
from personal.forms import Formulario_personal

def create_personal(request):
    if request.method == 'POST':
        form = Formulario_personal(request.POST)

        if form.is_valid():
            Personal.objects.create(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                puesto=form.cleaned_data['puesto']
            )
            return redirect(listar_personal)

    elif request.method == 'GET':  
        form = Formulario_personal()
        context={'form':form}
        return render(request, 'personal/crear_personal.html', context=context)

def listar_personal(request):
    listar_personal= Personal.objects.all()
    context={
        'listar_personal':listar_personal
    }
    return render(request, 'personal/listar_personal.html', context=context)
