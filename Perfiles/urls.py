from django.urls import path
from Perfiles import views

urlpatterns = [
    path('listar_perfiles/', views.listarPerfiles, name="listar-Perfiles"),
    path('nuevo_perfil/', views.nuevoPerfil, name="Nuevo_Perfil"),
    path('formEditarPerfil/<int:Id>', views.detalle_edicionP, name="form-Editar-Perfil"),
    path('editar_perfil/', views.editarPerfil, name="Editar_Perfil"),
    path('form_eliminar_Perfil/<int:Id>', views.detalle_eliminacionP, name="form-Eliminar-Perfil"),
    path('eliminar_perfil/<Id>', views.eliminarPerfil, name="Eliminar_Perfil"),
]