from .models import Operaciones
from Lotes.models import Lotes
from django.db.models import Sum, F

def operaciones_disponibles(request):
    qs = Operaciones.objects.annotate(
        Cantidad_Procesada = Sum('proceso_operacion__Cantidad_Procesada'),
        Pendientes=F('NumeroOperacionnes') - Sum('proceso_operacion__Cantidad_Procesada'),
        )
    return({'listado': qs})
    
    

     
