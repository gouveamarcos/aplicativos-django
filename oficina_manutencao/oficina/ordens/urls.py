from django.urls import path
from .views import pesquisar_os, abrir_ordem_servico  # Agora importando as duas funções

urlpatterns = [
    path('pesquisar/', pesquisar_os, name='pesquisar_os'),
    path('abrir/', abrir_ordem_servico, name='abrir_os'),  # Rota para abrir OS restaurada
]


