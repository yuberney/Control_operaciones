

from django.db.models import Sum, F
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView
from Operaciones.models import Operaciones
from Procesos.models import Procesos
from Lotes.models import Lotes
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def listaOperaciones(request):
      operacion = Operaciones.objects.filter(Activo = True).select_related('Lote')
      return render (request, "operaciones/listoperaciones.html", {'operaciones':operacion})

def filtarOperaciones(request, Id ):
      filtroOperaciones = Operaciones.objects.all().filter(Lote_id = Id, Activo = True)
      return render (request, "operaciones/filtro_referencia.html", {'filtroOperaciones':filtroOperaciones})

@login_required
def formOperaciones(request, Id):
    lote = Lotes.objects.get(pk=Id)
    proceso = Procesos.objects.all()  
    return render(request, "operaciones/crear_operacion.html",{'lotes':lote, 'procesos':proceso}) 

@login_required
def nueva_operacion(request):
            usuarioResponsable = request.user.pk
            fechaRegistro = request.POST['txtFechaRegistro']
            referencia = request.POST['txtReferencia']
            tipoOperacion = request.POST['txtTipoProceso']
            numeroOperaciones = request.POST['txtNumeroOperacion']
            precioOperacion = request.POST['txtPrecioOperacion']
        
            operacion = Operaciones.objects.create(
            FechaRegistro = fechaRegistro,
            Lote_id = referencia,
            Proceso_id = tipoOperacion,
            NumeroOperacionnes = numeroOperaciones,
            Precio = precioOperacion,
            UsuarioResponsable_id = usuarioResponsable

        )
            messages.success(request, "Operacion Creada Correctamente")
            return redirect('Lista-Lotes')

@login_required
def detalle_edicion(request, Id):
    operacion = Operaciones.objects.get(pk=Id)
    procesos = Procesos.objects.all()
    lote = Lotes.objects.filter(Activo = True)
    return render(request, "operaciones/editar_operacion.html",{
        'operacion': operacion, 
        'procesos' : procesos,
        'lotes' : lote
    })

@login_required
def editar_operacion(request):
        fechaRegistro = request.POST['txtFecha']
        referencia = request.POST["txReferencia"]
        tipoOperacion = request.POST['txtTipoOperacion']
        numeroOperacionnes = request.POST['txtNumeroOperacionnes']
        valorOperacion = request.POST['txtPrecio']
        id = request.POST["Id"]

        Operaciones.objects.filter(pk=id).update(
        Id = id,
        FechaRegistro = fechaRegistro,
        Lote_id = referencia,
        Proceso_id = tipoOperacion,
        NumeroOperacionnes = numeroOperacionnes,
        Precio = valorOperacion

    )
        messages.success(request, "Operacion Actualizado Correctamente")
        return redirect('Lista-Operaciones')

@login_required
def detalle_eliminacion(request, Id):
    operacion = Operaciones.objects.get(pk=Id)
    return render(request, "operaciones/eliminar_operacion.html",{
        'operacion': operacion, 
    })

@login_required
def eliminar_operacion(request, Id):
    Operaciones.objects.filter(pk=Id).update(
         Activo = False
    )
    messages.success(request, "Operacion Eliminada Correctamente")
    return redirect('Lista-Operaciones')
       
