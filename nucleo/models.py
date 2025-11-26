from django.db import models

class Pedido(models.Model):
    nombre = models.CharField(max_length=50)
    comida = models.CharField(max_length=80)
    direccion = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.comida}"
