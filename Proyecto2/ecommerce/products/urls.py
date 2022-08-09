from django.urls import path
from products.views import create_products, listar_productos, search_products

urlpatterns = [
    path('listar_productos/',listar_productos,name="listarproductos"),
    path('crear_producto/',create_products,name="createproducts"),
    path('search-products/',search_products,name='search_products' ),
]
