
from django.shortcuts import render, redirect
from .models import Pedido

def home(request):
    return render(request, "nucleo/home.html")

def ordenar(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        comida = request.POST["comida"]
        direccion = request.POST["direccion"]

        Pedido.objects.create(
            nombre=nombre,
            comida=comida,
            direccion=direccion
        )

        return redirect("home")

    return render(request, "nucleo/order.html")
