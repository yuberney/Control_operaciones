from django.urls import path
from Clientes import views

urlpatterns = [
    path('listar_clientes/', views.listar_clientes, name="listar_Clientes"),
    path('formClientes/', views.formCliente, name="FormNuevo_Cliente"),
    path('nuevo_cliente/', views.nuevo_cliente, name="Registrar_Cliente"),
    path('form_detalle_edicion/<Id>', views.form_detalle_edicion, name="Form_Detalle_Edicion"),
    path('editar_cliente/', views.editar_cliente, name="Editar_Cliente"),
    path('form_detalle_eliminacion/<Id>', views.form_detalle_eliminacionC, name="Form_Detalle_EliminacionC"),
    path('eliminar_cliente/<Id>', views.eliminar_cliente, name="Eliminar_Cliente"),
  
]