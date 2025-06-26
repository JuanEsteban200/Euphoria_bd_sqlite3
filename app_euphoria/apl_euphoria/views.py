from django.shortcuts import render









# Create your views here.
# productos
def productos(request):
    return render(request, 'productos.html')

# administrador
def administrador(request):
    return render(request, 'administrador.html')
#compras
def compras(request):
    return render(request, 'compras.html')
# ventas
def ventas(request):
    return render(request, 'ventas.html')
#vendedor
def vendedor(request):
    return render(request, 'vendedor.html')

# clientes
def Cliente(request):
    return render(request,'clientes.html')

#proveedor
def Proveedor(request):
    return render(request,'proveedores.html')

#pedido
def pedido(request):
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
def pqr(request):
    return render(request,'pqr.html')

