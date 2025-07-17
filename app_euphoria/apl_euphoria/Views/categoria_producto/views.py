from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from django.views.generic import ListView
from apl_euphoria.models import CategoriaProducto
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy


class CategoriaProductoListView(ListView):
    model = CategoriaProducto
    template_name = "Categoria_productos/lista_categoria.html"
    context_object_name = 'categoria_productos'   
    
    def get_queryset(self):
        return self.model.objects.all()
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Lista de Categorias'
       
       return context

class CategoriaProductoCreateView(CreateView):
    model = CategoriaProducto
    template_name = "Categoria_productos/crear.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:categoria_lista')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Crear Categoria'
       
       return context
<<<<<<< HEAD
    
=======
>>>>>>> bafcb17cf7b4e7b1b645f2b8e34bd24f4723947b
class CategoriaProductoUpdateView(UpdateView):
    model = CategoriaProducto
    template_name = "Categoria_productos/editar.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:categoria_lista')
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Editar Categoria'
       
       return context
<<<<<<< HEAD
    
=======
>>>>>>> bafcb17cf7b4e7b1b645f2b8e34bd24f4723947b
class CategoriaProductoDeleteView(DeleteView):
    model = CategoriaProducto
    template_name = "Categoria_productos/eliminar.html"
    success_url = reverse_lazy('apl_euphoria:categoria_lista')
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Eliminar Categoria'
       
       return context
<<<<<<< HEAD
    
=======
>>>>>>> bafcb17cf7b4e7b1b645f2b8e34bd24f4723947b
