from django.shortcuts import render
# Create your views here.
# productos
def Productos(request):
    return render(request, 'productos.html')

# administrador
def Administrador(request):
    return render(request, 'administrador.html')
#compras
def Compras(request):
    return render(request, 'compras.html')
# ventas
def Ventas(request):
    return render(request, 'ventas.html')
#vendedor
def Vendedor(request):
    return render(request, 'vendedor.html')

# clientes
def Cliente(request):
    return render(request,'clientes.html')

#proveedor
def Proveedor(request):
    return render(request,'proveedores.html')

#pedido
def Pedido(request):
    return render(request,'pedidos.html')

#pago
def Pago(request):
    return render(request,'pagos.html')

#factura
def Factura(request):
    return render(request,'factura.html')

#detallepedido
def DetallePedido(request):
    return render(request,'detallepedido.html')
#pqr
def Pqr(request):
    return render(request,'pqr.html')
#marca cosmeticos
def Marcacosmeticos(request):
    return render(request,'marcacosmeticos.html')

