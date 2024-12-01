from django.shortcuts import render
from .models import Pelicula

# Create your views here.

def catalogo(request):
    peliculas = Pelicula.objects.all()
    context={"peliculas" : peliculas}
    return render(request, 'pages/catalogo.html', context)