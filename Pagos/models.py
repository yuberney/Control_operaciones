from django.db import models
from datetime import datetime
from Proceso_Operacion.models import Proceso_Operacion

# Create your models here.

class Pagos(models.Model):
    Id = models.AutoField(primary_key=True)
    FechaPago = models.DateField('%Y-%m-%d')
    Empleado = models.CharField(max_length=50)
    Valor_Procesos = models.IntegerField()
    Otros_pagos = models.IntegerField()
    Descuentos = models.IntegerField()
    Valor_Total_Pagar = models.IntegerField()
    Observaciones = models.TextField()
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now_add=True)

    
    
    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"



  

   


        


