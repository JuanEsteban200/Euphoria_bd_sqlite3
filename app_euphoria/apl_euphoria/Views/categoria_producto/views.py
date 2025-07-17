from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect,render
from django.views.generic import ListView
from apl_euphoria.models import CategoriaProducto
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

# lista de categoria de productos
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
#crear categoria
class CategoriaProductoCreateView(CreateView):
    model = CategoriaProducto
    template_name = "Categoria_productos/crear.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:categoria_lista')
    
    #formato del mensaje de swetalert2
    def form_valid(self, form):
        messages.success(self.request, '¡Categotegoria creada con éxito!')
        return super().form_valid(form)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Crear Categoria'
       
       return context
# actualizar categoria  
class CategoriaProductoUpdateView(UpdateView):
    model = CategoriaProducto
    template_name = "Categoria_productos/editar.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:categoria_lista')
    
    #formato del mensaje de swetalert2
    def form_valid(self, form):
        messages.success(self.request, '¡Categoria editada con éxito!')
        return super().form_valid(form)
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Editar Categoria'
       
       return context
#eliminar categoria
class CategoriaProductoDeleteView(DeleteView):
    model = CategoriaProducto
    template_name = "Categoria_productos/eliminar.html"
    success_url = reverse_lazy('apl_euphoria:categoria_lista')
    
    #formato del mensaje de swetalert2
    def form_valid(self, form):
        messages.success(self.request, '¡Categoria eliminada con éxito!')
        return super().form_valid(form)
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Eliminar Categoria'
       
       return context
    
