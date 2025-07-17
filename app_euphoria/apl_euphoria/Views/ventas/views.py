from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from apl_euphoria.models import Venta
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

# Vista para listar productos
class VentaListView(ListView):
    model = Venta
    template_name = "Ventas/lista_ventas.html"
    context_object_name = 'pedidos'   
    
    def get_queryset(self):
        return self.model.objects.all()
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Lista de Ventas'
       
       return context
# crear producto
class VentaCreateView(CreateView):
    model = Venta
    template_name = "Ventas/crear.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:venta_lista')
    
    #formato del mensaje de swetalert2
    def form_valid(self, form):
        messages.success(self.request, '¡Venta creada con éxito!')
        return super().form_valid(form)
     
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Crear Venta'
       
       return context
#   
class VentaUpdateView(UpdateView):
    model = Venta
    template_name = "Ventas/editar.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:venta_lista')
    
    #formato del mensaje de swetalert2
    def form_valid(self, form):
        messages.success(self.request, '¡Venta editada con éxito!')
        return super().form_valid(form)
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Editar Venta'
       
       return context
    
    
    
class VentaDeleteView(DeleteView):
    model = Venta
    template_name = "Ventas/eliminar.html"
    success_url = reverse_lazy('apl_euphoria:venta_lista')
    
    #formato del mensaje de swetalert2
    def form_valid(self, form):
        messages.success(self.request, '¡Venta eliminada con éxito!')
        return super().form_valid(form)
    
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Eliminar Venta'
       
       return context
