from django.contrib import admin
from django.urls import path, include
from . import views  # Importa as views da pasta 'oficina'

urlpatterns = [
    path('admin/', admin.site.urls),  # Rota do painel de administração
    path('', views.home, name='home'),  # Página inicial
    path('clientes/', include('clientes.urls')),  # Inclui as URLs do app 'clientes'
    path('ordens/', include('ordens.urls')),  # Inclui as URLs do app 'ordens'
]
