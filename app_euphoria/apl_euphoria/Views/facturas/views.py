# Importación de módulos necesarios de Django
from django.views.decorators.csrf import csrf_exempt  
from django.shortcuts import render, redirect  
from apl_euphoria.models import Factura  
from django.contrib import messages  
from django.http import JsonResponse 
from django.urls import reverse_lazy  
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 
from django.utils.decorators import method_decorator  
from django.forms import ModelForm  


# Vista basada en clase para listar facturas 
class FacturaListView(ListView):
    model = Factura  
    template_name = 'Facturas/listar_facturas.html' 
    context_object_name = 'facturas'  
    # paginate_by = 10  # Número de clientes por página (comentado)

    # Método para agregar contexto adicional al template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        context['titulo'] = 'Lista de facturas'  
        context['Factura'] = 'Factura' 
        return context

    # Método decorado para interceptar todas las peticiones
    @method_decorator(csrf_exempt)  # Exime de protección CSRF
    def dispatch(self, request, *args, **kwargs):
        print("Interceptando en dispatch") 
        return super().dispatch(request, *args, **kwargs)
    
    # Maneja las peticiones GET con posibilidad de búsqueda
    def get(self, request, *args, **kwargs):
        search = request.GET.get('b', '') 
        if search:
            self.object_list = Factura.objects.filter(nombre__icontains=search)
        else: 
            self.object_list = Factura.objects.all()
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)

# Vista para crear nuevas facturas
class FacturaCreateView(CreateView):
    model = Factura  
    template_name = 'Facturas/crear.html'  
    fields = '__all__'  
    success_url = reverse_lazy('apl_euphoria:factura_lista')  

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
        print("Entrando al POST")  # 
        return super().post(request, *args, **kwargs)

    # Agrega contexto adicional al template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Crear nueva Factura'  
        context["mensaje"] = 'Ingrese los datos del formulario'  
        return context

# Vista para editar facturas existentes
class FacturaUpdateView(UpdateView):
    model = Factura  
    template_name = 'Facturas/editar.html'  
    fields = '__all__'  
    success_url = reverse_lazy('apl_euphoria:factura_lista')  

    # Mensaje de éxito que se mostrará con SweetAlert2
    def form_valid(self, form):
        messages.success(self.request, '¡Producto editado exitosamente!')
        return super().form_valid(form)

    # Método decorado para interceptar peticiones
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        print("Entrando al método dispatch") 
        return super().dispatch(request, *args, **kwargs)

    # Maneja peticiones GET (mostrar formulario con datos)
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
        context['titulo'] = 'Editar Factura'  
        context['mensaje'] = 'Actualiza la información de la Factura'  
        return context

# Vista para eliminar facturas
class FacturaDeleteView(DeleteView):
    model = Factura  
    template_name = 'Facturas/eliminar.html' 
    success_url = reverse_lazy('apl_euphoria:factura_lista')  

   # Agrega mensaje de éxito que se mostrará con SweetAlert2
    def form_valid(self, form):
        messages.success(self.request, '¡Producto Eliminado exitosamente!')
        return super().form_valid(form)
 
    # Método para interceptar peticiones
    def dispatch(self, request, *args, **kwargs):
        print("Interceptando en dispatch") 
        return super().dispatch(request, *args, **kwargs)
     
    # Agrega contexto adicional al template
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex ['titulo'] = 'Eliminar Factura'  
        return contex