from django.urls import path
from Lotes import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('listado_lotes/', views.listaLotes, name='Lista-Lotes'),
    path('detalle_lotes/<int:Id>', views.detalleLotes, name='detalle-Lotes'),
    path('formLotes/',views.formLote, name="FormLotes"),
    path('nuevo_lote/', views.nuevo_lote, name="Nuevo-Lote"),
    path('form_detalle_edicion/<int:Id>',views.detalle_edicion, name="Form-Detalle-EdicionLote"),
    path('editar-lote/',views.editar_lote, name="Editar-Lote"),
    path('form_detalle_eliminacion/<int:Id>',views.detalle_eliminacionLote, name="Form-Detalle-EliminacionLote"),
    path('eliminar-lote/<Id>',views.eliminar_lote, name="Eliminar-Lote"),
    path('form_detalle_completar/<int:Id>',views.detalle_completarLote, name="Form-Detalle-CompletarLote"),
    path('completar-lote/',views.completar_lote, name="Completar-Lote"),
    path('listado_lotes_completos/', views.LotesCompletos, name='Lista-Lotes-Completos'),
]