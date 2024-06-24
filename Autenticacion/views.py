from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def registrarUsuario(request):
    if request.method == 'GET' :
        return render(request, "registration/registrarUsuario.html", { 'form' : UserCreationForm })
    else:
        if request.POST["password1"] != request.POST["password2"]:
            return render(request, "registration/registrarUsuario.html", { 'form' : UserCreationForm , 'mensaje' : "Las Contraseñas no Coinciden"})
        else:
            usuario = request.POST["username"]
            clave = request.POST["password1"]
            user = User.objects.create_user(username = usuario, password = clave)
            user.save()
            return render(request, "registration/registrarUsuario.html", { 'form' : UserCreationForm , 'mensaje' : "Usuario Creado con exito"})

def iniciarSesion(request):
    if request.method == 'GET' :
       return render(request, "registration/login.html", { 'form' : AuthenticationForm }) 
    else:
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(username = usuario, password = clave)
        if user is None:
            return render(request, "registration/login.html", { 'form' : AuthenticationForm, 'mensaje' : "Usuario o Password Incorrectos"}) 
        else:
            login(request, user)
            return redirect('Index')
        
def cerrarSesion(request):
    logout(request)
    return redirect('Login')
            

