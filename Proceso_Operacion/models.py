from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from Operaciones.models import Operaciones
from Usuarios.models import Usuario
# Create your models here.

class Proceso_Operacion(models.Model):
    Id = models.AutoField(primary_key=True)
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Referencia = models.ForeignKey(Operaciones, on_delete=models.CASCADE)
    Cantidad_Procesada = models.IntegerField()
    Estado = models.CharField(max_length=100, default='Pendiente Aprobar')
    FechaRegistro = models.DateField('%d-%m-%Y')
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now_add=True)

    @property
    def valorTotalProcesado(self):
        valorTotal = self.Cantidad_Procesada * self.Referencia.Precio
        return valorTotal

    class Meta:
        verbose_name = "Proceso Operacion"
        verbose_name_plural = "Procesos Operaciones"