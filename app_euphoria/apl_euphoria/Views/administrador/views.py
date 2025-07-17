from django.shortcuts import render
from django.http import HttpResponse
from apl_euphoria.models import Administrador
from django.urls import reverse_lazy   
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class AdministradorListView(ListView):
    model = Administrador
    template_name = "Administrador/listar_administrador.html"
    context_object_name = 'administradores'   
    
    def get_queryset(self):
        return self.model.objects.all()
    
    
class AdministradorCreateView(CreateView):
    model = Administrador
    template_name = "Administrador/agregar.html"
    fields = '__all__'
        
    def get_success_url(self):
        return reverse_lazy('apl_euphoria:lista_administrador')
        

class AdministradorUpdateView(UpdateView):
    model = Administrador
    template_name = "Administrador/editar.html"
    fields = '__all__'
    
    def get_success_url(self):
        return reverse_lazy('apl_euphoria:lista_administrador')
class AdministradorDeleteView(DeleteView):
    model = Administrador
    template_name = "Administrador/eliminar.html"
    
    def get_success_url(self):
        return reverse_lazy('apl_euphoria:lista_administrador')
    