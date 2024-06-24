from django.db import models
from Lotes.models import Lotes
from Usuarios.models import Usuario
from Procesos.models import Procesos

 
  
# Create your models here.
class Operaciones(models.Model):
    Id = models.AutoField(primary_key=True)
    FechaRegistro = models.DateField('%Y-%m-%d')
    Lote = models.ForeignKey(Lotes, on_delete = models.PROTECT)
    Proceso = models.ForeignKey(Procesos, on_delete = models.CASCADE)
    NumeroOperacionnes = models.IntegerField()
    Precio = models.IntegerField()
    UsuarioResponsable = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    Activo = models.IntegerField(default=True)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now_add=True)

    @property
    def CantidadProcesada(self):
        from django.db.models import Sum
        from Proceso_Operacion.models import Proceso_Operacion
        sumaProcesado = Proceso_Operacion.objects.filter(Referencia = self).aggregate(
            totalProcesados = Sum('Cantidad_Procesada', default=0))
        return sumaProcesado
    
    @property
    def CantidadOperaciones(self):
       totalOperaciones = self.NumeroOperacionnes * self.Lote.Cantidad_Registrada
       return totalOperaciones
    
    
        
    """
    @property
    def Faltantes(self):
        from Lotes.models import Lotes
        from django.db.models import Sum
        pendientes = Lotes.objects.filter(Referencia = self).aggregate(Pendientes = Sum('Cantidad_Registrada')-Sum('Cantidad_Procesada'))
        return pendientes
    """
    

    def __str__(self):
        return self.Lote.Referencia

    class Meta:
        verbose_name = "Operacion"
        verbose_name_plural = "Operaciones" 