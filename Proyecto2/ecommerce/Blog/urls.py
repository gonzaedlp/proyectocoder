from django.urls import path
from Blog.views import create_article, listar_articulos

urlpatterns = [
    path('listar_articulos/',listar_articulos,name="la"),
    path('crear_articulo/',create_article,name="ca"),
]
