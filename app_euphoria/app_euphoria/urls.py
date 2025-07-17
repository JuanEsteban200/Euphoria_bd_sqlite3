from django.contrib import admin
from django.urls import path, include
from apl_euphoria.views import index, gestion
urlpatterns = [
    path('admin/', admin.site.urls),
        # Rutas generales (index y home)
    path('index/', index, ), 

    path('gestion/', include('apl_euphoria.urls')),  # Ruta base para todo lo de apl_euphoria
]
