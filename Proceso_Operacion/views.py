from django.shortcuts import render, redirect
from django.views.generic import ListView
from Proceso_Operacion.models import Proceso_Operacion
from Usuarios.models import Usuario
from django.contrib import messages
from Operaciones.models import Operaciones
from django.contrib.auth.decorators import login_required 



# Create your views here.


class PendienteAprobar(ListView):
    model = Proceso_Operacion
    context_object_name = 'procesoOperacion'
    template_name = "proceso_operacion/procesos_pendientes_aprobar.html"
    queryset = Proceso_Operacion.objects.filter(Estado = 'Pendiente Aprobar').select_related('Referencia')


class ProcesosPendientePagar(ListView):
    model = Proceso_Operacion
    context_object_name = 'pendiente_Pagar'
    template_name = "proceso_operacion/pendientes_pagar.html"
    queryset = Proceso_Operacion.objects.filter(Estado = 'Aprobado').select_related('Referencia')
   

class Pendiente_aprobar_por_Empleado(ListView):
    model = Proceso_Operacion
    template_name = "proceso_operacion/procesos_pendientes_aprobar_Empleado.html"

    def get(self, request, *args, **kwargs):
        proceso_Pendiente_aprobar = Proceso_Operacion.objects.filter(Estado = 'Pendiente Aprobar', Usuario = request.user.pk)
        return render(request,self.template_name,{'proceso_Pendiente_aprobar':proceso_Pendiente_aprobar})


@login_required
def formProceso_Operaciones(request, Id):
    operacion = Operaciones.objects.get(pk=Id)
    return render(request, "proceso_operacion/crear_proceso_operacion.html", {'operacion':operacion})

@login_required
def crear_proceso_operacion(request):
       empleado = request.user.pk
       cantidadProcesada = request.POST['txtCantidad_Procesada']
       referencia = request.POST['txtReferencia']
       fecha = request.POST['txtFecha']
       
       nuevo_proceso = Proceso_Operacion.objects.create(
        Usuario_id = empleado,
        Cantidad_Procesada = cantidadProcesada,
        Referencia_id = referencia,
        FechaRegistro = fecha
        
    )
       messages.success(request, "Proceso Registrado Correctamente")
       return redirect('Lista-Lotes')

@login_required
def detalle_edicionProceso(request, Id):
    empleado = Usuario.objects.all()
    proceso = Proceso_Operacion.objects.get(pk=Id)
    return render(request, "proceso_operacion/editar_proceso_operacion.html",{
        'procesoOperacion': proceso,
        'empleado':empleado
    })

@login_required
def editar_proceso_operacion(request):
        fecha = request.POST['txtFecha']
        empleado = request.POST['txtEmpleado']
        referencia = request.POST['txtReferencia']
        cantidadProcesada = request.POST['txtCantidad_Procesada']
        id = request.POST["Id"]

        Proceso_Operacion.objects.filter(pk=id).update(
        Id = id,
        FechaRegistro = fecha,
        Usuario_id = empleado,
        Referencia_id = referencia,
        Cantidad_Procesada= cantidadProcesada
    )
        messages.success(request, "Proceso Operacion Actualizado Correctamente")
        return redirect('Operaciones_Pendientes_Liquidar')


@login_required
def detalle_eliminacionProceso(request, Id):
    proceso = Proceso_Operacion.objects.get(pk=Id)
    return render(request, "proceso_operacion/eliminar_proceso_operacion.html",{
        'procesos': proceso
    })

@login_required
def eliminarProceso(request, Id):
    proceso = Proceso_Operacion.objects.get(pk=Id)
    proceso.delete()
    messages.success(request, "Proceso Eliminado Correctamente")
    return redirect('Operaciones_Pendientes_Liquidar') 

@login_required
def liquidar_proceso_operacion(request, Id):
    Proceso_Operacion.objects.filter(pk=Id).update(
         Estado = 'Aprobado'
    )
    messages.success(request, "Operacion Arpobada Correctamente")
    return redirect('Operaciones_Pendientes_Aprobar')


