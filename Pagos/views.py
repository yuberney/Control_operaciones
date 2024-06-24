from django.shortcuts import render, redirect
from Pagos.models import Pagos
from Usuarios.models import Usuario
from Proceso_Operacion.models import Proceso_Operacion
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.



@login_required
def formNuevo_Pago(request, pk):
    qs = Proceso_Operacion.objects.all().filter(Estado = 'Liquidado', Usuario = pk)
    valor_pagar = 0
    for item in qs:
         valor_pagar += item.valorTotalProcesado
    user  = Usuario.objects.get(Id = pk)
    return render(request, "pagos/crear_pago.html", { 'us': user, 'valpago': valor_pagar })


@login_required
def nevo_pago(request):
    Empleado = request.POST["txtEmpleado"]
    ValorProcesos = request.POST["txtValorProcesos"]
    OtrosPagos = request.POST["txtOtrosPagos"]
    Descuentos = request.POST["txtDescuentos"]
    ValorTotal = request.POST["txtValorPagar"]
    DetallesPagos = request.POST["txtDetallesPagos"]

    pago = Pagos.objects.create(
        Empleado = Empleado,
        Valor_Procesos = ValorProcesos,
        Otros_pagos = OtrosPagos,
        Descuentos = Descuentos,
        Valor_Total_Pagar = ValorTotal,
        Observaciones = DetallesPagos
    )

    messages.success(request, "Pago Registrado Correctamente")
    return redirect('listar_Pagos')
    
