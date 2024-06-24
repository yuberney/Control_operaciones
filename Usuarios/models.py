from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from Perfiles.models import Perfiles


# Create your models here.

class Usuario(AbstractUser):
    Id = models.AutoField(primary_key=True)
    Tipo_documento = models.CharField('Tipo de Documento', max_length=50, null=True)
    Documento = models.IntegerField('Documento', unique=True, null=True)
    Telefono = models.IntegerField('Telefono', null=True )
    Fecha_nacimiento = models.DateField('Fecha Nacimiento', null=True)
    Perfil = models.ForeignKey(Perfiles, on_delete=models.CASCADE, null=True)
    Salario = models.CharField('Salario', max_length=50, null=True)
    Numero_cuenta = models.IntegerField('Cuenta', null=True)
    Banco = models.CharField('Banco', max_length=50, null=True)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"