from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'), 
    path('home/', views.home, name='home'),
    path('pedido/', views.pedido_detalle, name='pedido_detalle'),
    path('rastreo/', views.rastreo, name='rastreo'),
]
