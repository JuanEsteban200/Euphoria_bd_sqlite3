from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from apl_euphoria.models import Producto
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

# Vista para listar productos
class ProductoListView(ListView):
    model = Producto
    template_name = "Productos/lista_productos.html"
    context_object_name = 'productos'   
    
    def get_queryset(self):
        return self.model.objects.all()
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Lista de Productos'
       
       return context
# crear producto
class ProductoCreateView(CreateView):
    model = Producto
    template_name = "Productos/crear.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:producto_lista')
    
    #formato del mensaje de swetalert2
    def form_valid(self, form):
        messages.success(self.request, '¡Producto creado con éxito!')
        return super().form_valid(form)
     
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Crear Producto'
       
       return context
#   
class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "Productos/editar.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:producto_lista')
    
    #formato del mensaje de swetalert2
    def form_valid(self, form):
        messages.success(self.request, '¡Producto editado con éxito!')
        return super().form_valid(form)
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Editar Producto'
       
       return context
    
    
    
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "Productos/eliminar.html"
    success_url = reverse_lazy('apl_euphoria:producto_lista')
    
    #formato del mensaje de swetalert2
    def form_valid(self, form):
        messages.success(self.request, '¡Producto eliminado con éxito!')
        return super().form_valid(form)
    
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Eliminar Producto'
       
       return context
