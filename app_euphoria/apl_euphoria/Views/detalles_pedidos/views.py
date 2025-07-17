from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from apl_euphoria.models import DetallePedido
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

# Vista para listar productos
class Detalles_pedidoListView(ListView):
    model =  DetallePedido
    template_name = "Detalles_pedidos/listar_detalle.html"
    context_object_name = 'pedidos'   
    
    def get_queryset(self):
        return self.model.objects.all()
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Lista de Detalles de Pedidos'
       
       return context
# crear producto
class DetallespedidoCreateView(CreateView):
    model = DetallePedido
    template_name = "Detalles_pedidos/crear.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:detalle_pedido_lista')
    
    #formato del mensaje de swetalert2
    def form_valid(self, form):
        messages.success(self.request, '¡Detalle del pedido creado con éxito!')
        return super().form_valid(form)
     
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Crear Detalle del Pedido'
       
       return context
#   
class DetallespedidoUpdateView(UpdateView):
    model = DetallePedido
    template_name = "Detalles_pedidos/editar.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:detalle_pedido_lista')
    
    #formato del mensaje de swetalert2
    def form_valid(self, form):
        messages.success(self.request, '¡Detalle del pedido editado con éxito!')
        return super().form_valid(form)
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Editar Detalle del Pedido'
       
       return context
    
    
    
class DetallespedidoDeleteView(DeleteView):
    model = DetallePedido
    template_name = "Detalles_pedidos/eliminar.html"
    success_url = reverse_lazy('apl_euphoria:detalle_pedido_lista')
    
    #formato del mensaje de swetalert2
    def form_valid(self, form):
        messages.success(self.request, '¡detalles del pedido eliminado con éxito!')
        return super().form_valid(form)
    
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Eliminar Detalle del Pedido'
       
       return context
