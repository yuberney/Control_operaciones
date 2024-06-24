from django.db import models

# Create your models here.
class Perfiles(models.Model):
    Id = models.AutoField(primary_key = True)
    Nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Nombre 
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
