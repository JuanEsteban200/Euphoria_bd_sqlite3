from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from django.views.generic import ListView
from apl_euphoria.models import Compra
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy


class CompraListView(ListView):
    model = Compra
    template_name = "Compras/listar_compras.html"
    context_object_name = 'compra_list'

    def get_queryset(self):
        return self.model.objects.all()

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        print("Interceptando en dispatch")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'COMPRAS'
        return context

class CompraCreateView(CreateView):
    model = Compra
    template_name = "Compras/crear.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:compra_lista')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        print("Interceptando en dispatch")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear compra'
        return context
class CompraUpdateView(UpdateView):
    model = Compra
    template_name = "Compras/editar.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:compra_lista')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        print("Interceptando en dispatch")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar compra'
        return context
class CompraDeleteView(DeleteView):
    model = Compra
    template_name = "Compras/eliminar.html"
    success_url = reverse_lazy('apl_euphoria:compra_lista')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        print("Interceptando en dispatch")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar compra'
        return context
