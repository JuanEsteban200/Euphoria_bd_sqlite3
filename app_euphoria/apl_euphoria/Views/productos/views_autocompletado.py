from dal import autocomplete
from apl_euphoria.models import CategoriaProducto, MarcaCosmetico

class CategoriaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = CategoriaProducto.objects.all()
        if self.q:  # Si el usuario está escribiendo algo (`q` es el parámetro de búsqueda)
            qs = qs.filter(nombre__icontains=self.q)
        return qs

class MarcaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = MarcaCosmetico.objects.all()
        if self.q:
            qs = qs.filter(nombre__icontains=self.q)
        return qs