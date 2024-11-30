from django.db import models

# Create your models here.

class Usuario(models.Model):
    rut         = models.IntegerField(null=False, unique=True, primary_key=True)
    dv_rut      = models.CharField(max_length=1, null=False)
    nombre      = models.CharField(max_length=40, null=False)
    appaterno   = models.CharField(max_length=50, null=False)
    apmaterno   = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f'Rut: {self.rut}-{self.dv_rut} | Nombre: {self.nombre} {self.appaterno}'

class Cliente(models.Model):
    usuario     = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    email_cli   = models.EmailField(max_length=50, unique=True, null=False)

    def __str__(self):
        return f'{self.usuario} | Email: {self.email_cli}'