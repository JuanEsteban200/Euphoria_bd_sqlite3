from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from django.views.generic import ListView
from apl_euphoria.models import Pqr
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy


class PqrListView(ListView):
    model = Pqr
    template_name = "Pqr/listar_pqr.html"
    context_object_name = 'pqr_list'

    def get_queryset(self):
        return self.model.objects.all()

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        print("Interceptando en dispatch")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = ' PQRS'
        return context

class PqrCreateView(CreateView):
    model = Pqr
    template_name = "Pqr/crear.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:pqr_lista')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        print("Interceptando en dispatch")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear PQR'
        return context
class PqrUpdateView(UpdateView):
    model = Pqr
    template_name = "Pqr/editar.html"
    fields = '__all__'
    success_url = reverse_lazy('apl_euphoria:pqr_lista')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        print("Interceptando en dispatch")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar PQR'
        return context
class PqrDeleteView(DeleteView):
    model = Pqr
    template_name = "Pqr/eliminar.html"
    success_url = reverse_lazy('apl_euphoria:pqr_lista')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        print("Interceptando en dispatch")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar PQR'
        return context
