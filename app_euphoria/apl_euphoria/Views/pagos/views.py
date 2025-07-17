# Importación de módulos necesarios de Django
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from apl_euphoria.models import Pago
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.forms import ModelForm



# Vista basada en clase para listar Pagos
class PagoListView(ListView):
    model = Pago
    template_name = 'Pagos/listar_pago.html'
    context_object_name = 'pagos'
    # paginate_by = 10  # Número de clientes por página

# Método para agregar contexto adicional al template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Pagos'
        context['Pago'] = 'Pago'
        return context

    # dispatch método para interceptar las peticiones
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       print("Interceptando en dispatch")
       
       return super().dispatch(request, *args, **kwargs)
    
     # Maneja las peticiones GET con posibilidad de búsqueda
    def get(self, request, *args, **kwargs):
        search = request.GET.get('b', '')
        if search:
            self.object_list = Pago.objects.filter(nombre__icontains=search)
        else:
            self.object_list = Pago.objects.all()
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)
    

    #def get_queryset(self):
        #query = self.request.GET.get('q')  # recibe lo que se escribe en el buscador
       # if query:
         #   return Cliente.objects.filter(nombre__icontains=query)
        #return Cliente.objects.all()
        
    
# Vista para crear nuevos pagos  
class PagoCreateView(CreateView):
    model = Pago
    template_name = 'Pagos/crear.html'
    fields = '__all__'  
    success_url =  reverse_lazy('apl_euphoria:pago_lista')  # Redirige a la lista al guardar
    
    # Mensaje de éxito que se mostrará con SweetAlert2
    def form_valid(self, form):
        messages.success(self.request, '¡Producto creado con éxito!')
        return super().form_valid(form)
    

    # Método decorado para interceptar peticiones
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        print("Interceptando en dispatch")
        return super().dispatch(request, *args, **kwargs)

     # Maneja peticiones GET (mostrar formulario vacío)
    def get(self, request, *args, **kwargs):
        print("Entrando al GET")
        return super().get(request, *args, **kwargs)
    
    # Maneja peticiones POST (procesar formulario)
    def post(self, request, *args, **kwargs):
        print("Entrando al POST")
        return super().post(request, *args, **kwargs)
    
     # Agrega contexto adicional al template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Crear nuevo pago'
        context["mensaje"] = 'Ingrese los datos del formulario'
        return context
    


# Vista para editar pagos existentes
class PagoUpdateView(UpdateView):
    model = Pago
    template_name = 'Pagos/editar.html'
    fields = '__all__'  # Puedes especificar los campos que deseas incluir
    success_url = reverse_lazy('apl_euphoria:pago_lista')  # Redirige a la lista al guardar
    
    # Mensaje de éxito que se mostrará con SweetAlert2
    def form_valid(self, form):
        messages.success(self.request, '¡Producto editado exitosamente!')
        return super().form_valid(form)
    
    # Método decorado para interceptar peticiones
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        print("Entrando al método dispatch")
        return super().dispatch(request, *args, **kwargs)
    
     # Maneja peticiones GET (mostrar formulario vacío)
    def get(self, request, *args, **kwargs):
        print("Método GET ejecutado - mostrar formulario con datos")
        return super().get(request, *args, **kwargs)
    
        # Maneja peticiones POST (procesar formulario)
    def post(self, request, *args, **kwargs):
        print("Método POST ejecutado - procesar formulario")
        return super().post(request, *args, **kwargs)
 
    # Agrega contexto adicional al template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Pago'
        context['mensaje'] = 'Actualiza la información del Pago'
        return context
    
# Vista para eliminar pagos 
class PagoDeleteView(DeleteView):
    model = Pago
    template_name = 'Pagos/eliminar.html'
    success_url = reverse_lazy('apl_euphoria:pago_lista')  # Redirige a la lista de clientes
    
    # Mensaje de éxito que se mostrará con SweetAlert2
    def form_valid(self, form):
        messages.success(self.request, '¡Producto Eliminado exitosamente!')
        return super().form_valid(form)
  
    # Método decorado para interceptar peticiones
    def dispatch(self, request, *args, **kwargs):
        print("Interceptando en dispatch")
        
        return super().dispatch(request, *args, **kwargs)
    
    # Agrega contexto adicional al template  
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex ['titulo'] = 'Eliminar Pago'
        
        return contex





















