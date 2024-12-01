from django.shortcuts import render, get_object_or_404
from pagWeb.models import Pelicula

# Create your views here.

def reserva(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    return render(request, 'pages/reserva.html', {'pelicula':pelicula})
