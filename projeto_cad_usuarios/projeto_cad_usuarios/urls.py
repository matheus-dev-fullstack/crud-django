

from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    #rota, view responsável, nome de referência 
    #path é o que vem depois da raiz do projeto depois do /
    #path vaio é página inicial
    path('', views.home, name='home'),
]
