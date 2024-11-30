from django.db import models
from appClientes import Usuario

# Create your models here.

class Vendedor(models.Model):
    usuario     = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    sueldo      = models.IntegerField(null=False, max_length=8)

    def __str__(self):
        return f'{self.usuario} | Sueldo: {self.sueldo}'