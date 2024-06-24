from django.urls import path
from Control_operacionesApp import views

urlpatterns = [
     path('index/',views.index, name="Index"), 
      
]