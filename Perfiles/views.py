from django.shortcuts import render, redirect
from Perfiles.models import Perfiles
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def listarPerfiles(request):
    perfiles = Perfiles.objects.all()
    return render (request, "perfiles/perfiles.html", {'perfil':perfiles})

@login_required
def nuevoPerfil(request):
    perfil = request.POST['txtNombre']
    query = Perfiles.objects.filter(Nombre = perfil).exists()

    if(query == False):
        nombre = Perfiles.objects.create(
        Nombre = perfil
      )
        messages.success(request, "Perfil Registrado Correctamente")
        return redirect('listar-Perfiles')
    else:
        messages.success(request, "El Perfil ya se encuentra registrado")
        return redirect('listar-Perfiles')

@login_required
def detalle_edicionP(request, Id):
    perfil = Perfiles.objects.get(pk=Id)
    return render(request, "perfiles/editar_perfil.html",{
        'perfil': perfil
    })
@login_required
def editarPerfil(request):
     perfil = request.POST["txtNombre"]
     id = request.POST["Id"]
     query = Perfiles.objects.filter(Nombre = perfil).exists()

     if(query == False):
            Perfiles.objects.filter(pk=id).update(
            Id=id,
            Nombre = perfil
            )
            messages.success(request, "Perfil Actualizado Correctamente")
            return redirect('listar-Perfiles')
     else:
        messages.success(request, "No se puede actualizar el perfil, ya existe un registro con el mismo nombre")
        return redirect('listar-Perfiles')
@login_required
def detalle_eliminacionP(request, Id):
    perfil = Perfiles.objects.get(pk=Id)
    return render(request, "perfiles/eliminar_perfil.html",{
        'perfil': perfil
    })
@login_required
def eliminarPerfil(request, Id):
    perfil = Perfiles.objects.get(pk=Id)
    perfil.delete()
    messages.success(request, "Perfil Eliminado Correctamente")
    return redirect('listar-Perfiles') 