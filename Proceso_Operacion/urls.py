from django.urls import path
from Proceso_Operacion import views
from django.contrib.auth.decorators import login_required
from .views import PendienteAprobar,ProcesosPendientePagar,Pendiente_aprobar_por_Empleado


urlpatterns = [
    path('operaciones-Pendientes-aprobar/', login_required(PendienteAprobar.as_view()), name="Operaciones_Pendientes_Aprobar"),
    path('operaciones-pendientes-pagar/', login_required(ProcesosPendientePagar.as_view()), name="Operaciones_Pendientes_Pagar"),
    path('operaciones-Pendientes-aprobar-porEmpleado/', login_required(Pendiente_aprobar_por_Empleado.as_view()), name="Operaciones_Pendientes_Aprobar_PorEmpleado"),
    path('formProceso-Operaciones/<int:Id>', views.formProceso_Operaciones, name="FormProcesos_Operaciones"),
    path('crear-proceso-operaciones/', views.crear_proceso_operacion, name="Nuevo_Proceso_Operacion"),
    path('form_edicion_Proceso-Operaciones/<Id>', views.detalle_edicionProceso, name="Form_Edicion_Procesos_Operaciones"),
    path('editar_Proceso_Operaciones/', views.editar_proceso_operacion, name="Editar_Proceso_Operaciones"),
    path('liquidar-proceso-operaciones/<Id>', views.liquidar_proceso_operacion, name="Liquidar_Proceso_Operacion"),
    path('form_Eliminar_Proceso_Operaciones/<Id>', views.detalle_eliminacionProceso, name="Form_Eliminar_Proceso_Operaciones"),
    path('Eliminar_Proceso_Operaciones/<Id>', views.eliminarProceso, name="Eliminar_Proceso_Operaciones"),

]  