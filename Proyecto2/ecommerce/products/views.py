from django.shortcuts import render, redirect
from products.models import Products
from products.forms import Formulario_productos

def create_products(request):
    if request.method == 'POST':
        form = Formulario_productos(request.POST)

        if form.is_valid():
            Products.objects.create(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price']
            )
            return redirect(listar_productos)

    elif request.method == 'GET':  
        form = Formulario_productos()
        context={'form':form}
        return render(request, 'products/crear_producto.html', context=context)

def listar_productos(request):
    listar_productos= Products.objects.all()
    context={
        'listar_productos':listar_productos
    }
    return render(request, 'products/listar_productos.html', context=context)

def primer_formulario(request):
    return render(request, 'primer_formulario.html', context={})

def search_products(request):
    search=request.GET['search']
    products=Products.objects.filter(name__icontains=search)
    context={
        "products":products
        }
    return render(request, 'products/search_products.html',context=context)