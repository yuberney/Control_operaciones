from django.urls import path
from Operaciones import views


urlpatterns = [
    path('lista_operaciones/',views.listaOperaciones, name="Lista-Operaciones"), 
    path('filtro_operaciones/<Id>',views.filtarOperaciones, name="Filtro-Operaciones"), 
    path('formOperaciones/<Id>',views.formOperaciones, name="formOperaciones"),
    path('nueva-operacion/', views.nueva_operacion, name="Nueva_Operacion"),
    path('form_detalle_edicion/<int:Id>',views.detalle_edicion, name="Form-Detalle-Edicion"),
    path('editar-operacion/',views.editar_operacion, name="Editar_Operacion"),
    path('form_detalle_eliminacion/<int:Id>',views.detalle_eliminacion, name="Form-Detalle-Eliminacion"),
    path('eliminar-operacion/<Id>',views.eliminar_operacion, name="Eliminar_Operacion"),
]