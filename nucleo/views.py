from django.shortcuts import render, redirect

def login_page(request):
    return render(request, "nucleo/login.html") 

def home(request):
    return render(request, "nucleo/home.html")

def pedido_detalle(request):
    return render(request, "nucleo/pedido.html")

def rastreo(request): 
    return render(request, "nucleo/repartidor.html")