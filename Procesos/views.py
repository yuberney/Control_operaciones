from django.shortcuts import render, redirect
from Procesos.models import Procesos
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def listarProcesos(request):
    procesos = Procesos.objects.all()
    return render (request, "procesos/procesos.html", {'procesos':procesos})

@login_required
def nuevoProceso(request):
    nombre = request.POST['txtNombre']
    query = Procesos.objects.filter(Nombre = nombre).exists()

    if(query == False):
        nombre = Procesos.objects.create(
        Nombre = nombre
      )
        messages.success(request, "Proceso Registrado Correctamente")
        return redirect('lista-Procesos')
    else:
        messages.success(request, "El Proceso ya se encuentra registrado")
        return redirect('lista-Procesos')

@login_required
def detalle_edicionProcesos(request, Id):
    proceso = Procesos.objects.get(pk=Id)
    return render(request, "procesos/editar_proceso.html",{
        'proceso': proceso
    })
@login_required
def editarProceso(request):
    nombre = request.POST["txtNombre"]
    id = request.POST["Id"]
    query = Procesos.objects.filter(Nombre = nombre).exists()

    if(query == False):
            Procesos.objects.filter(pk=id).update(
            Id=id,
            Nombre = nombre
            )
            messages.success(request, "Proceso Actualizado Correctamente")
            return redirect('lista-Procesos')
    else:
        messages.success(request, "No se puede actualizar el perfil, ya existe un registro con el mismo nombre")
        return redirect('lista-Procesos')
@login_required
def detalle_eliminacionProceso(request, Id):
    proceso = Procesos.objects.get(pk=Id)
    return render(request, "procesos/eliminar_proceso.html",{
        'proceso': proceso
    })
@login_required
def eliminarProceso(request, Id):
    proceso = Procesos.objects.get(pk=Id)
    proceso.delete()
    messages.success(request, "Proceso Eliminado Correctamente")
    return redirect('lista-Procesos') 
