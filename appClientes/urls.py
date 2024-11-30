from django.urls import path
from . import views

urlpatterns = [
    path('reservar', views.reserva, name='reservar')
]