from django.shortcuts import render
from django.http import HttpResponse
from apl_euphoria.models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.

class ClienteListView(ListView):
    model = 'Cliente'
    template_name = "Clientes/lista_cliente.html"
    context_object_name = 'clientes'   
    
    def get_queryset(self):
        return self.model.objects.all() 

class ClienteCreateView(CreateView):
    model = 'Cliente'
    template_name = "Clientes/crear_cliente.html"
    fields = '__all__'
    success_url = '/clientes/'          
class ClienteUpdateView(UpdateView):
    model = 'Cliente'
    template_name = "Clientes/editar_cliente.html"
    fields = '__all__'
    success_url = '/clientes/'
class ClienteDeleteView(DeleteView):
    model = 'Cliente'
    template_name = "Clientes/eliminar_cliente.html"
    success_url = '/clientes/'
