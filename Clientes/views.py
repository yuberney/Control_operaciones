from django.shortcuts import render,redirect
from Clientes.models import Clientes
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def listar_clientes(request):
    clientes = Clientes.objects.filter(Activo ='1')
    return render(request, "clientes/clientes.html",{'clientes':clientes})

@login_required
def formCliente(request):
    return render(request, "clientes/crear_cliente.html")

@login_required
def nuevo_cliente(request):
    """Quey para verficar que el cliente no exista en la bd"""
    nit = request.POST["txtNit"]
    nombreEmpresa = request.POST["txtNombreEmpresa"]
    query = Clientes.objects.filter(Nit_Empresa = nit).exists()

    if(query == False):
        nit = request.POST["txtNit"]
        nombreEmpresa = request.POST["txtNombreEmpresa"]
        direccion = request.POST["txtDireccion"]
        representante =request.POST["txtRepresentante"]
        telefono = request.POST["txtTelefono"]
        
        cliente = Clientes.objects.create(
        Nit_Empresa = nit,
        Nombre_Empresa = nombreEmpresa,
        Direccion = direccion,
        Representante = representante,
        Telefono = telefono,
       
    )
        messages.success(request, "Cliente creado correctamente")
        return redirect('listar_Clientes')
    else:
        messages.success(request, "El Cliente ya se encuentra Registrado")
        return redirect('listar_Clientes')

@login_required
def form_detalle_edicion(request, Id):
    cliente = Clientes.objects.get(pk=Id)
    return render(request, "clientes/editar_cliente.html",{'cliente': cliente})

@login_required
def editar_cliente(request):
        nit = request.POST["txtNit_Empresa"]
        nombreEmpresa = request.POST["txtNombre_Empresa"]
        direccion = request.POST["txtDireccion"]
        representante =request.POST["txtRepresentante"]
        telefono = request.POST["txtTelefono"]
        id = request.POST["Id"]
        
        Clientes.objects.filter(pk=id).update(
        Id = id,
        Nit_Empresa = nit,
        Nombre_Empresa = nombreEmpresa,
        Direccion = direccion,
        Representante = representante,
        Telefono = telefono,
    )
        messages.success(request, "Cliente Actualizado Correctamente")
        return redirect('listar_Clientes')

@login_required
def form_detalle_eliminacionC(request, Id):
    cliente = Clientes.objects.get(pk=Id)
    return render(request, "clientes/eliminar_cliente.html",{
        'cliente': cliente
    })

@login_required
def eliminar_cliente(request, Id):
    Clientes.objects.filter(pk=Id).update(
         Activo = False
    )
    messages.success(request, "Cliente Eliminado Correctamente")
    return redirect('listar_Clientes')
