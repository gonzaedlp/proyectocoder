from django.shortcuts import render, redirect
from Blog.models import Articles
from Blog.forms import Formulario_articles

def create_article(request):
    if request.method == 'POST':
        form = Formulario_articles(request.POST)
        if form.is_valid():
            Articles.objects.create(
            titulo=form.cleaned_data['titulo'], 
            descripcion=form.cleaned_data['descripcion'],
            autor=form.cleaned_data['autor']
            )
            return redirect(listar_articulos)

    elif request.method == 'GET':  
        form = Formulario_articles()
        context={'form':form}
        return render(request, 'Blog/crear_articulo.html', context=context)


def listar_articulos(request):
    listar_articulos= Articles.objects.all()
    context={
        'listar_articulos':listar_articulos
    }
    return render(request, 'Blog/listar_articulos.html', context=context)

