from django.urls import path
from Pagos import views

urlpatterns = [
    path('form_nuevo_pago/<int:pk>/', views.formNuevo_Pago, name="Form-Nuevo-Pago"),
    #path('nuevo_pago/', views.nevo_pago, name="Nuevo_Pago"),
]