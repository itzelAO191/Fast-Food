from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'), 
    path('home/', views.home, name='home'),
    path('pedido/', views.pedido_detalle, name='pedido_detalle'),
    path('rastreo/', views.rastreo, name='rastreo'),
    path('registrar/', views.usuario, name='registrar_usuario'),
    path('buscar/', views.buscar_user, name='buscar_user'),
    path('editar/<int:user_id>/', views.editar_user, name='editar_user'),
    path('eliminar/<int:user_id>/', views.eliminar_user, name='eliminar_user'),
]
