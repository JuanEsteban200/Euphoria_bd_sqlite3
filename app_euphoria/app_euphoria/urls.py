"""
URL configuration for app_euphoria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apl_euphoria.views import productos, administrador, compras, Cliente, Proveedor, pedido, Pago, Factura, DetallePedido,ventas,vendedor, pqr, Categoria

urlpatterns = [
    path('admin/', admin.site.urls),
    path('administrador/', administrador),#modulo administrador
    path('productos/', productos),#modulo productos
    path('compras/', compras),#modulo compras
    path('ventas/', ventas),#modulo ventas
    path('vendedor/', vendedor),#modulo vendedor
    path('Clientes/', Cliente),
    path('Proveedores/', Proveedor),
    path('Pedidos/', pedido),
    path('Pago/', Pago),
    path('Factura/', Factura),
    path('Detallepedido/', DetallePedido),
    path('pqr/', pqr),
    path('Categoria/', Categoria),

]
