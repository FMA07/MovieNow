from django.db import models
from appClientes.models import Usuario

# Create your models here.

class Vendedor(models.Model):
    usuario     = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    sueldo      = models.IntegerField(null=False)

    def __str__(self):
        return f'{self.usuario} | Sueldo: {self.sueldo}'