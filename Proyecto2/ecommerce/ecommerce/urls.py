from django.contrib import admin
from django.urls import path, include
from ecommerce.views import base


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',base ,name="saludo"),
    path('products/', include('products.urls')),
    path('Blog/', include('Blog.urls')),
    path('personal/', include('personal.urls')),


]
