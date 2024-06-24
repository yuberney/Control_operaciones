from django.shortcuts import render,redirect
from Usuarios.models import Usuario
from Perfiles.models import Perfiles
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def listar_usuarios(request):
    usuarios = Usuario.objects.filter(is_active='1')
    return render(request, "usuarios/usuarios.html",{'usuarios':usuarios})

@login_required
def formUsuario(request):
    perfil = Perfiles.objects.all()
    return render(request, "usuarios/crear_usuario.html",{'perfiles':perfil})


@login_required
def nuevo_usuario(request):
    """Quey para verficar que el usuario no exista en la bd"""
    documento = request.POST["txtIdentificacion"]
    query = Usuario.objects.filter(Documento = documento).exists()

    if(query == False):
        tipoDocumento = request.POST["txtTipo_identificacion"]
        documento = request.POST["txtIdentificacion"]
        nombre = request.POST["txtNombres"]
        apellidos =request.POST["txtApellidos"]
        telefono = request.POST["txtTelefono"]
        fechaNacimiento = request.POST["txtFecha_nacimiento"]
        perfil = request.POST["txtPerfil"]
        salario = request.POST["txtSalario"]
        numeroCuenta = request.POST["txtNumero_cuenta"]
        banco = request.POST["txtBanco"]
        usuario = request.POST["txtUsuario"]
        clave = request.POST["txtContraseña"]

        user = Usuario.objects.create(
        Tipo_documento = tipoDocumento,
        Documento = documento,
        first_name = nombre,
        last_name = apellidos,
        Telefono = telefono,
        Fecha_nacimiento = fechaNacimiento,
        Perfil_id = perfil,
        Salario = salario,
        Numero_cuenta = numeroCuenta,
        Banco = banco,
        username = usuario,
        password = clave
    )
        messages.success(request, "Empleado creado correctamente")
        return redirect('listar_Usuarios')
    else:
        messages.success(request, "El Empleado ya se encuentra Registrado")
        return redirect('listar_Usuarios')

@login_required
def form_detalle_edicionU(request, Id):
    usuario = Usuario.objects.get(pk=Id)
    perfil = Perfiles.objects.all()
    return render(request, "usuarios/editar_usuario.html",{'usuario': usuario ,'perfiles': perfil})

@login_required
def editar_usuario(request):
        tipoDocumento = request.POST["txtTipo_identificacion"]
        documento = request.POST["txtIdentificacion"]
        nombre = request.POST["txtNombres"]
        apellidos =request.POST["txtApellidos"]
        telefono = request.POST["txtTelefono"]
        fechaNacimiento = request.POST["txtFecha_nacimiento"]
        perfil = request.POST["txtPerfil"]
        salario = request.POST["txtSalario"]
        numeroCuenta = request.POST["txtNumero_cuenta"]
        banco = request.POST["txtBanco"]
        usuario = request.POST["txtUsuario"]
        id = request.POST["Id"]

        Usuario.objects.filter(pk=id).update(
        Id = id,
        Tipo_documento = tipoDocumento,
        Documento = documento,
        first_name = nombre,
        last_name = apellidos,
        Telefono = telefono,
        Fecha_nacimiento = fechaNacimiento,
        Perfil_id = perfil,
        Salario = salario,
        Numero_cuenta = numeroCuenta,
        Banco = banco,
        username = usuario,
    )
        messages.success(request, "Usuario Actualizado Correctamente")
        return redirect('listar_Usuarios')

@login_required
def form_detalle_eliminacionU(request, Id):
    usuario = Usuario.objects.get(pk=Id)
    return render(request, "usuarios/eliminar_usuario.html",{
        'usuario': usuario
    })

@login_required
def eliminar_usuario(request, Id):
    Usuario.objects.filter(pk=Id).update(
         is_active = False
    )
    messages.success(request, "Usuario Eliminado Correctamente")
    return redirect('listar_Usuarios')
