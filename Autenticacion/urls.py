from django.urls import path
from Autenticacion import views

urlpatterns = [
    path('registrar/', views.registrarUsuario, name='Registrar-Usuario'),
    path('', views.iniciarSesion, name='Login'),
    path('salir/', views.cerrarSesion, name='Cerrar-Sesion'),
]