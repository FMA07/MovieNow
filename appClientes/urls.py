from django.urls import path
from . import views

urlpatterns = [
    path('reservar/<int:id>/', views.reserva, name='reservar')
]