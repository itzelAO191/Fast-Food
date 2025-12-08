from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from django.db.models import Q

def login_page(request):
    return render(request, "nucleo/login.html") 

def home(request):
    return render(request, "nucleo/home.html")

def pedido_detalle(request):
    return render(request, "nucleo/pedido.html")

def rastreo(request): 
    return render(request, "nucleo/repartidor.html")

def usuario(request):

    if request.method == 'POST':
        vnombre = request.POST['nombre']
        vapellido = request.POST['apellido']
        vemail = request.POST['email']
        vdireccion = request.POST['direccion']
        vtelefono = request.POST['telefono']
        vpassword = request.POST['password']

        usuario_nuevo = Usuario(
            nombre=vnombre,
            apellido=vapellido,
            email=vemail,
            direccion=vdireccion,
            telefono=vtelefono,
            password=vpassword
        )

        usuario_nuevo.save()

        return render(request, "nucleo/registrarUser.html",{
            'mensaje': "Usuario registrado correctamente"
        })
    return render(request, "nucleo/registrarUser.html")

def  buscar_user(request):
    resultados = []
    query = request.GET.get('consultar_usuario')

    if query:
        resultados = Usuario.objects.filter(
            Q(nombre__icontains=query) | Q(apellido__icontains=query) | Q(email__icontains=query) | Q(telefono__icontains=query)
        )
    return render(request, "nucleo/buscar_user.html", {'resultados': resultados})

def editar_user(request, user_id):
    usuario = get_object_or_404(Usuario, id=user_id)

    if request.method == 'POST':
        usuario.nombre = request.POST.get('nombre', usuario.nombre)
        usuario.apellido = request.POST.get('apellido', usuario.apellido)
        usuario.email = request.POST.get('email', usuario.email)
        usuario.direccion = request.POST.get('direccion', usuario.direccion)
        usuario.telefono = request.POST.get('telefono', usuario.telefono)
        usuario.password = request.POST.get('password', usuario.password)

        usuario.save()

        return redirect('buscar_user')
    
    return render(request, "nucleo/editar_user.html", {'usuario': usuario})

def eliminar_user(request, user_id):
    usuario_a_borrar = get_object_or_404(Usuario, id=user_id)

    if request.method == 'POST':
        usuario_a_borrar.delete()
        return redirect('buscar_user')
    return  render (request, "nucleo/eliminar_user.html", {'usuario': usuario_a_borrar})
