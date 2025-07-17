from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from apl_euphoria.models import Promocion
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

# Vista para listar promociones
class PromocionListView(ListView):
    model = Promocion
    template_name = "Promociones/lista_promociones.html"
    context_object_name = 'promociones'   
    
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
# crear promocion
class PromocionCreateView(CreateView):
    model = Promocion
    template_name = "Promociones/crear.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:promocion_lista')

    #formato del mensaje de swetalert2
    def form_valid(self, form):
        messages.success(self.request, '¡Promoción creada con éxito!')
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
class PromocionUpdateView(UpdateView):
    model = Promocion
    template_name = "Promociones/editar.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:promocion_lista')

    #formato del mensaje de swetalert2
    def form_valid(self, form):
        messages.success(self.request, '¡Promoción editada con éxito!')
        return super().form_valid(form)
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Editar Producto'
       
       return context
    


class PromocionDeleteView(DeleteView):
    model = Promocion
    template_name = "Promocion/eliminar.html"
    success_url = reverse_lazy('apl_euphoria:promocion_lista')

    #formato del mensaje de swetalert2
    def form_valid(self, form):
        messages.success(self.request, '¡Promoción eliminada con éxito!')
        return super().form_valid(form)
    
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['titulo'] = 'Eliminar Producto'
       
       return context
