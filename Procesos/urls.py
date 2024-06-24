from django.urls import path
from Procesos import views

urlpatterns = [
    path('listar_procesos/', views.listarProcesos, name="lista-Procesos"),
    path('nuevo_proceso/', views.nuevoProceso, name="Nuevo_Proceso"),
    path('formEditarProceso/<int:Id>', views.detalle_edicionProcesos, name="Form-Editar-Proceso"),
    path('editar_proceso/', views.editarProceso, name="Editar_Proceso"),
    path('form_eliminar_Proceso/<int:Id>', views.detalle_eliminacionProceso, name="Form-Eliminar-Proceso"),
    path('eliminar_proceso/<Id>', views.eliminarProceso, name="Eliminar_Proceso"),
]