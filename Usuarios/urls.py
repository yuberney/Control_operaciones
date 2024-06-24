from django.urls import path
from Usuarios import views

urlpatterns = [
    path('listar_usuarios/', views.listar_usuarios, name="listar_Usuarios"),
    path('formUsuarios/', views.formUsuario, name="FormNuevo_Usuario"),
    path('nuevo_usuario/', views.nuevo_usuario, name="Registrar_Usuario"),
    path('form_detalle_edicion/<Id>', views.form_detalle_edicionU, name="Form_Detalle_EdicionU"),
    path('editar_usuario/', views.editar_usuario, name="Editar_Usuario"),
    path('form_detalle_eliminacion/<Id>', views.form_detalle_eliminacionU, name="Form_Detalle_EliminacionU"),
    path('eliminar_usuario/<Id>', views.eliminar_usuario, name="Eliminar_Usuario"),
  
]