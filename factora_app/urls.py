from django.urls import path, include #Libreria para utilizar path manejo de urls
from django.conf import settings #Configuracion de nuestro proyecto
from . import views #Importamos nuestras vistas
app_name = 'factora_app' #El nombre de nuestra aplicacion

urlpatterns = [
    path('',views.principal, name='principal'),
]
