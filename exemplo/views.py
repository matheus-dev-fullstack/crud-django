# from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from exemplo.models import Cliente

class ClienteList(ListView):
    model = Cliente
    queryset = Cliente.objects.all()  # método que será utilizado para buscar os clientes
    
class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('exemplo:list')