from django.db import models

# Create your models here.

class Pelicula(models.Model):
    cod_pelicula    = models.CharField(max_length=5, null=False, unique=True)
    titulo          = models.CharField(max_length=30, null=False)
    director        = models.CharField(max_length=50)
    reparto         = models.CharField(max_length=200)
    descripcion     = models.CharField(max_length=200)
    disponibilidad  = models.BooleanField(null=False)

    def __str__(self):
        return f'Cod: {self.cod_pelicula} | Título: {self.titulo}'

class Catalogo(models.Model):
    cod_local       = models.CharField(null=False, max_length=6) #CODIGO DE LA TIENDA DONDE SE ENCUENTRA EL CATÁLOGO. A FUTURO PUEDE SER LLAVE FORÁNEA
    Pelicula        = models.ManyToManyField(Pelicula, related_name="catalogos")

    def __str__(self):
        return f'Codigo de local: {self.cod_local}'