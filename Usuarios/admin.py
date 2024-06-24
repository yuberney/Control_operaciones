from django.contrib import admin
from Usuarios.models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('Usuario__first_name',)
# Register your models here.

admin.site.register(Usuario, UsuarioAdmin)