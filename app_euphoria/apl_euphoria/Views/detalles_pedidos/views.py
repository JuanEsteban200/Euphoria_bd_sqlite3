from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from apl_euphoria.models import  DetallePedido
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

class Detalle_PedidoListView(ListView):
    model = DetallePedido
    template_name = "detalles_pedidos/listar_detalle.html"
    context_object_name = 'detalles_pedido'   
    
    def get_queryset(self):
        return self.model.objects.all()
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Lista de detalles de pedidos'
       
       return context
class Detalle_PedidoCreateView(CreateView):
    model = DetallePedido
    template_name = "detalles_pedidos/crear.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:detalle_pedido_lista')
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Crear Detalle del Pedido'
       
       return context
class Detalle_PedidoUpdateView(UpdateView):
    model = DetallePedido
    template_name = "detalles_pedidos/editar.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:detalle_pedido_lista')
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Editar Detalle del Pedido'
       
       return context
class Detalle_PedidoDeleteView(DeleteView):
    model = DetallePedido
    template_name = "detalles_pedidos/eliminar.html"
    success_url = reverse_lazy('apl_euphoria:detalle_pedido_lista')
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Eliminar Detalle del Pedido'
       
       return context
