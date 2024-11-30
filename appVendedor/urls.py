from django.urls import path
from . import views

urlpatterns = [
    path('arrendar', views.arriendo, name='arrendar')
]