from django.db.models import Sum, F
from django.shortcuts import render
from django.shortcuts import render, redirect
from Clientes.models import Clientes
from Lotes.models import Lotes

from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required
def listaLotes(request):
      lotes = Lotes.objects.filter(Activo = True, Estado = 'Ingresado')
      return render(request, "lotes/lista_lotes.html", {'lotes':lotes})

@login_required
def detalleLotes(request, Id):
      lotes = Lotes.objects.filter(pk=Id)
      return render(request, "lotes/detalle_lote.html", {'lotes':lotes})

@login_required
def LotesCompletos(request):
      lotes = Lotes.objects.filter(Estado = 'Completado')
      return render(request, "lotes/lotes_completos.html", {'lotes':lotes})

@login_required
def formLote(request):
    clientes = Clientes.objects.filter(Activo = True)
    return render(request, "lotes/crear_lote.html",{'clientes':clientes}) 

@login_required
def nuevo_lote(request):
            cliente = request.POST['txtCliente']
            referencia = request.POST['txtReferencia']
            descripcion = request.POST['txtDescripcion']
            cantidadRegistrada  = request.POST['txtCantidad_Resgistrada']
            fechaIngreso = request.POST['txtFechaIngreso']
            fechaSalida = request.POST['txtFechaSalida']
            fechaEntregado = request.POST['txtFechaEntregado']
            usuarioResponsable = request.user.pk

            lote = Lotes.objects.create(
            Cliente_id = cliente,
            Referencia = referencia,
            Descripcion = descripcion,
            Cantidad_Registrada= cantidadRegistrada,
            FechaIngreso = fechaIngreso,
            FechaSalida = fechaSalida,
            FechaEntregado = fechaEntregado,
            UsuarioResponsable_id = usuarioResponsable
        )
            messages.success(request, "Lote Creado Correctamente")
            return redirect('Lista-Lotes')
  
@login_required
def detalle_edicion(request, Id):
    lotes = Lotes.objects.get(pk=Id)
    cliente = Clientes.objects.all()
    return render(request, "lotes/editar_lotes.html",{
        'lotes': lotes, 'clientes':cliente
        
    })

@login_required
def editar_lote(request):
        cliente = request.POST['txtCliente']
        referencia = request.POST['txtReferencia']
        descripcion = request.POST['txtDescripcion']
        cantidadRegistrada  = request.POST['txtCantidad_Resgistrada']
        fechaIngreso = request.POST['txtFechaIngreso']
        fechaSalida = request.POST['txtFechaSalida']
        fechaEntregado = request.POST['txtFechaEntregado']
        id = request.POST["Id"]

        Lotes.objects.filter(pk=id).update(
        Id = id,
        Cliente_id = cliente,
        Referencia = referencia,
        Descripcion = descripcion,
        Cantidad_Registrada= cantidadRegistrada,
        FechaIngreso = fechaIngreso,
        FechaSalida = fechaSalida,
        FechaEntregado = fechaEntregado,
    )
        messages.success(request, "Lote Actualizado Correctamente")
        return redirect('Lista-Lotes')


@login_required
def detalle_eliminacionLote(request, Id):
    lotes = Lotes.objects.get(pk=Id)
    return render(request, "lotes/eliminar_lotes.html",{
        'lotes': lotes,
        
    })
   
@login_required
def eliminar_lote(request, Id):
    Lotes.objects.filter(pk=Id).update(
         Activo = False
    )
    messages.success(request, "Lote Eliminado Correctamente")
    return redirect('Lista-Lotes')



@login_required
def detalle_completarLote(request, Id):
    lotes = Lotes.objects.get(pk=Id)
    return render(request, "lotes/completarLote.html",{
        'lotes': lotes, 
    })
   
@login_required
def completar_lote(request):
        fechaEntregado = request.POST['txtFechaEntregado']
        id = request.POST["Id"]

        Lotes.objects.filter(pk=id).update(
        Id = id,
        FechaEntregado = fechaEntregado,
        Estado = 'Completado'
    )
        messages.success(request, "Lote Completado Correctamente")
        return redirect('Lista-Lotes')
    
