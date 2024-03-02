# from django.shortcuts import render
from django.views.generic import ListView

from exemplo.models import Cliente

class ClienteList(ListView):
    model = Cliente
    queryset = Cliente.objects.all()  # método que será utilizado para buscar os clientes
    