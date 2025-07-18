from django.urls import path
from apl_euphoria.views import index, gestion
from apl_euphoria.Views.cliente.views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView
from apl_euphoria.Views.productos.views import ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView
from apl_euphoria.Views.pedidos.views import PedidoListView, PedidoCreateView, PedidoUpdateView, PedidoDeleteView
from apl_euphoria.Views.detalles_pedidos.views import Detalle_PedidoListView, Detalle_PedidoCreateView, Detalle_PedidoUpdateView, Detalle_PedidoDeleteView
# from apl_euphoria.Views.pagos.views import PagoListView, PagoCreateView, PagoUpdateView, PagoDeleteView
# from apl_euphoria.Views.proveedores.views import ProveedorListView, ProveedorCreateView, ProveedorUpdateView, ProveedorDeleteView
from apl_euphoria.Views.compras.views import CompraListView, CompraCreateView, CompraUpdateView, CompraDeleteView
# from apl_euphoria.Views.facturas.views import FacturaListView, FacturaCreateView, FacturaUpdateView, FacturaDeleteView
# from apl_euphoria.Views.promociones.views import PromocionListView, PromocionCreateView, PromocionUpdateView, PromocionDeleteView
from apl_euphoria.Views.categoria_producto.views import CategoriaProductoListView, CategoriaProductoCreateView, CategoriaProductoUpdateView, CategoriaProductoDeleteView
from apl_euphoria.Views.marca_producto.views import MarcaCosmeticoListView, MarcaCosmeticoCreateView, MarcaCosmeticoUpdateView, MarcaCosmeticoDeleteView
from apl_euphoria.Views.pqr.views import PqrListView, PqrCreateView, PqrUpdateView, PqrDeleteView
from apl_euphoria.Views.administrador.views import AdministradorListView, AdministradorCreateView, AdministradorUpdateView, AdministradorDeleteView
# from apl_euphoria.Views.vendedor.views import VendedorListView, VendedorCreateView, VendedorUpdateView, VendedorDeleteView
from apl_euphoria.Views.ventas.views import VentaListView, VentaCreateView, VentaUpdateView, VentaDeleteView
app_name = 'apl_euphoria'

urlpatterns = [
    #  Administrador URLs
    path('administradores/', AdministradorListView.as_view(), name='lista_administrador'),
    path('administradores/crear/', AdministradorCreateView.as_view(), name='administrador_crear'),
    path('administradores/<int:pk>/editar/', AdministradorUpdateView.as_view(), name='administrador_editar'),
    path('administradores/<int:pk>/eliminar/', AdministradorDeleteView.as_view(), name='administrador_eliminar'),
    
    # # Vendedor URLs
    # path('vendedores/', VendedorListView.as_view(), name='vendedor_lista'),
    # path('vendedores/crear/', VendedorCreateView.as_view(), name='vendedor_crear'),
    # path('vendedores/<int:pk>/editar/', VendedorUpdateView.as_view(), name='vendedor_editar'),
    # path('vendedores/<int:pk>/eliminar/', VendedorDeleteView.as_view(), name='vendedor_eliminar'),
    
    # Venta URLs
     path('ventas/', VentaListView.as_view(), name='venta_lista'),
     path('ventas/crear/', VentaCreateView.as_view(), name='venta_crear'),
     path('ventas/<int:pk>/editar/', VentaUpdateView.as_view(), name='venta_editar'),
     path('ventas/<int:pk>/eliminar/', VentaDeleteView.as_view(), name='venta_eliminar'),
    
    # Cliente URLs
    path('clientes/', ClienteListView.as_view(), name='cliente_lista'),  
    path('clientes/crear/', ClienteCreateView.as_view(), name='cliente_crear'),  
    path('clientes/<int:pk>/editar/', ClienteUpdateView.as_view(), name='cliente_actualizar'),  
    path('clientes/<int:pk>/eliminar/', ClienteDeleteView.as_view(), name='cliente_eliminar'),  

    # Producto URLs
    path('productos/', ProductoListView.as_view(), name='producto_lista'), 
    path('productos/crear/', ProductoCreateView.as_view(), name='producto_crear'), 
    path('productos/<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto_editar'),  
    path('productos/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='producto_eliminar'), 
    

    # # Pedido URLs
     path('pedidos/', PedidoListView.as_view(), name='pedido_lista'),  
     path('pedidos/crear/', PedidoCreateView.as_view(), name='pedido_crear'),  
     path('pedidos/<int:pk>/editar/', PedidoUpdateView.as_view(), name='pedido_editar'),  
     path('pedidos/<int:pk>/eliminar/', PedidoDeleteView.as_view(), name='pedido_eliminar'),  

    # # Detalle Pedido URLs
     path('detalles-pedido/', Detalle_PedidoListView.as_view(), name='detalle_pedido_lista'), 
     path('detalles-pedido/crear/', Detalle_PedidoCreateView.as_view(), name='detalle_pedido_crear'),  
     path('detalles-pedido/<int:pk>/editar/', Detalle_PedidoUpdateView.as_view(), name='detalle_pedido_editar'),  
     path('detalles-pedido/<int:pk>/eliminar/', Detalle_PedidoDeleteView.as_view(), name='detalle_pedido_eliminar'),  

    # # Pago URLs
    # path('pagos/', PagoListView.as_view(), name='pago_lista'),  
    # path('pagos/crear/', PagoCreateView.as_view(), name='pago_crear'),  
    # path('pagos/<int:pk>/editar/', PagoUpdateView.as_view(), name='pago_editar'),  
    # path('pagos/<int:pk>/eliminar/', PagoDeleteView.as_view(), name='pago_eliminar'),  

    # # Proveedor URLs
    # path('proveedores/', ProveedorListView.as_view(), name='proveedor_lista'),  
    # path('proveedores/crear/', ProveedorCreateView.as_view(), name='proveedor_crear'),  
    # path('proveedores/<int:pk>/editar/', ProveedorUpdateView.as_view(), name='proveedor_editar'),  
    # path('proveedores/<int:pk>/eliminar/', ProveedorDeleteView.as_view(), name='proveedor_eliminar'),  

    # # Compra URLs
    path('compras/', CompraListView.as_view(), name='compra_lista'),
    path('compras/crear/', CompraCreateView.as_view(), name='compra_crear'),
    path('compras/editar/<int:pk>/', CompraUpdateView.as_view(), name='compra_editar'),
    path('compras/eliminar/<int:pk>/', CompraDeleteView.as_view(), name='compra_eliminar'), 

    # # Factura URLs
    # path('facturas/', FacturaListView.as_view(), name='factura_lista'),  
    # path('facturas/crear/', FacturaCreateView.as_view(), name='factura_crear'),  
    # path('facturas/<int:pk>/editar/', FacturaUpdateView.as_view(), name='factura_editar'),  
    # path('facturas/<int:pk>/eliminar/', FacturaDeleteView.as_view(), name='factura_eliminar'),  

    # # Promocion URLs
    # path('promociones/', PromocionListView.as_view(), name='promocion_lista'),  
    # path('promociones/crear/', PromocionCreateView.as_view(), name='promocion_crear'),  
    # path('promociones/<int:pk>/editar/', PromocionUpdateView.as_view(), name='promocion_editar'), 
    # path('promociones/<int:pk>/eliminar/', PromocionDeleteView.as_view(), name='promocion_eliminar'),  

    # Categoria Producto URLs
    path('categorias/', CategoriaProductoListView.as_view(), name='categoria_lista'),  
    path('categorias/crear/', CategoriaProductoCreateView.as_view(), name='categoria_crear'),  
    path('categorias/<int:pk>/editar/', CategoriaProductoUpdateView.as_view(), name='categoria_editar'),  
    path('categorias/<int:pk>/eliminar/', CategoriaProductoDeleteView.as_view(), name='categoria_eliminar'),  

    #  Marca Cosmetico URLs
    path('marcas/', MarcaCosmeticoListView.as_view(), name='marca_lista'),  
    path('marcas/crear/', MarcaCosmeticoCreateView.as_view(), name='marca_crear'),  
    path('marcas/<int:pk>/editar/', MarcaCosmeticoUpdateView.as_view(), name='marca_editar'),  
    path('marcas/<int:pk>/eliminar/', MarcaCosmeticoDeleteView.as_view(), name='marca_eliminar'),  

    # PQR URLs
    path('pqrs/', PqrListView.as_view(), name='pqr_lista'),
    path('pqrs/crear/', PqrCreateView.as_view(), name='pqr_crear'),
    path('pqrs/<int:pk>/editar/', PqrUpdateView.as_view(), name='pqr_editar'),
    path('pqrs/<int:pk>/eliminar/', PqrDeleteView.as_view(), name='pqr_eliminar'),
  
















]