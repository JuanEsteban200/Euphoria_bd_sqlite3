from django.shortcuts import render
























# Create your views here.
# clientes

def Cliente(request):
    return render(request,'clientes.html')

def Proveedor(request):
    return render(request,'proveedores.html')

def pedido(request):
    return render(request,'pedidos.html')

def Pago(request):
    return render(request,'pagos.html')

def Factura(request):
    return render(request,'factura.html')

def DetallePedido(request):
    return render(request,'detallepedido.html')

