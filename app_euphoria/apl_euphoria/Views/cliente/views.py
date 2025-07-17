from django.shortcuts import render
from django.http import HttpResponse
from apl_euphoria.models import Cliente
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.

class ClienteListView(ListView):
    model = Cliente
    template_name = "Clientes/lista_cliente.html"
    context_object_name = 'clientes'   
    
    def get_queryset(self):
        return self.model.objects.all() 

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = "Clientes/crear.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:cliente_lista')  # usa el nombre de tu url        
class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = "Clientes/editar.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:cliente_lista')  # usa el nombre de tu url        
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "Clientes/eliminar.html"
    success_url = reverse_lazy('apl_euphoria:cliente_lista')  # usa el nombre de tu url        
