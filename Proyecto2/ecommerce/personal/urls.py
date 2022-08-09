from django.urls import path
from personal.views import create_personal, listar_personal

urlpatterns = [
    path('listar_personal/',listar_personal,name="listarpersonal"),
    path('crear_personal/',create_personal,name="createpersonal"),
]
