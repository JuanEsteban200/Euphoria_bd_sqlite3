from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from apl_euphoria.models import Pedido
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib import messages

# Vista para listar productos
class PedidoListView(ListView):
    model = Pedido
    template_name = "Pedidos/listar_pedidos.html"
    context_object_name = 'pedidos'   
    
    def get_queryset(self):
        return self.model.objects.all()
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Lista de Pedidos'
       
       return context
# crear producto
class PedidoCreateView(CreateView):
    model = Pedido
    template_name = "Pedidos/crear.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:pedido_lista')
    
    #formato del mensaje de swetalert2
    def form_valid(self, form):
        messages.success(self.request, '¡Pedido creado con éxito!')
        return super().form_valid(form)
     
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Crear Pedido'
       
       return context
#   
class PedidoUpdateView(UpdateView):
    model = Pedido
    template_name = "Pedidos/editar.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:pedido_lista')
    
    #formato del mensaje de swetalert2
    def form_valid(self, form):
        messages.success(self.request, '¡Pedido editado con éxito!')
        return super().form_valid(form)
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Editar Pedido'
       
       return context
    
    
    
class PedidoDeleteView(DeleteView):
    model = Pedido
    template_name = "Pedidos/eliminar.html"
    success_url = reverse_lazy('apl_euphoria:pedido_lista')
    
    #formato del mensaje de swetalert2
    def form_valid(self, form):
        messages.success(self.request, '¡Pedido eliminado con éxito!')
        return super().form_valid(form)
    
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Eliminar Pedido'
       
       return context
