from django.db import models
from django.db import models
from Clientes.models import Clientes
from Usuarios.models import Usuario

# Create your models here.
class Lotes(models.Model):
    Id = models.AutoField(primary_key=True)
    Cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT)
    Referencia = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=100)
    Cantidad_Registrada = models.PositiveIntegerField(default=1)
    Estado = models.CharField(max_length=50, default='Ingresado')
    FechaIngreso = models.DateField('%d-%m-%Y')
    FechaSalida = models.DateField('%d-%m-%Y')
    FechaEntregado = models.DateField('%Y-%m-%d', null=True, blank=True)
    UsuarioResponsable = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    Activo = models.IntegerField(default=True)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now_add=True)

    def DiasAtrazo(self):
        diasAtrazo = self.FechaSalida - self.FechaEntregado
        return diasAtrazo

    def __str__(self):
        return self.Referencia
    
    class Meta:
        verbose_name = "Lote"
        verbose_name_plural = "Lotes" 