from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    password = models.CharField(max_length=128)

def __str__(self):
    return f"{self.nombre} {self.apellido} {self.email} {self.telefono}"