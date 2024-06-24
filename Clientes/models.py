from django.db import models

# Create your models here.
class Clientes(models.Model):
    Id = models.AutoField(primary_key=True)
    Nit_Empresa = models.IntegerField()
    Nombre_Empresa = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=100)
    Representante = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=100)
    Activo = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Nombre_Empresa
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes" 
