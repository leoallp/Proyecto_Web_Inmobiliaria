"""
URL configuration for proy_inmobiliaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#urls.py
from django.contrib import admin
from django.urls import path, include
from arriendo_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('actualizar_datos/', views.actualizar_datos, name='actualizar_datos'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', views.registro, name='registro'),
    path('', views.index, name='index'),
    path('filtrar-comunas/', views.filtrar_comunas, name='filtrar_comunas'),
    path('bienvenido/', views.bienvenido, name='bienvenido'),
    path('crear_inmueble/', views.crear_inmueble, name='crear_inmueble'),
    path('vista_arrendador/', views.vista_arrendador, name='vista_arrendador'),
    path('vista_arrendatario/', views.vista_arrendatario, name='vista_arrendatario'),
    path('inmuebles_disponibles/', views.inmuebles_disponibles, name='inmuebles_disponibles'),
    path('editar_inmueble/<int:inmueble_id>/', views.editar_inmueble, name='editar_inmueble'),

]
