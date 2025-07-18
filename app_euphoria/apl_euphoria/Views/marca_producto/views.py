from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from django.views.generic import ListView
from apl_euphoria.models import MarcaCosmetico
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy


class MarcaCosmeticoListView(ListView):
    model = MarcaCosmetico
    template_name = "Marca_productos/lista_marca.html"
    context_object_name = 'marca_cosmeticos'   
    
    def get_queryset(self):
        return self.model.objects.all()
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Lista de Marcas'
       
       return context

class MarcaCosmeticoCreateView(CreateView):
    model = MarcaCosmetico
    template_name = "Marca_productos/crear.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:marca_lista')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Registrar Marca'
       
       return context
class MarcaCosmeticoUpdateView(UpdateView):
    model = MarcaCosmetico
    template_name = "Marca_productos/editar.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:marca_lista')
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Editar Categoria'
       
       return context
class MarcaCosmeticoDeleteView(DeleteView):
    model = MarcaCosmetico
    template_name = "Marca_productos/eliminar.html"
    success_url = reverse_lazy('apl_euphoria:marca_lista')
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Eliminar Marca'
       
       return context
