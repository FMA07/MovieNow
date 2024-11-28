from django.urls import path
from . import views

urlPatterns = [
    path('catalogo', views.catalogo, name='Catalogo')
]