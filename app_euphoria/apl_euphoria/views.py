from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# productos
def productos(request):
    return render(request, 'productos.html')

# administrador
def adminitrador(request):
    return render(request, 'adminitrador.html')
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
def vista1(request):
    return HttpResponse("esta es mi primera vista")

def vista2(request):
    persona = {
        'nombre': 'Edward',
        'edad': 30,
        'correo': 'edward@example.com'
    }
    return HttpResponse(persona)

def vista3(request):
    return render(request, 'index.html')

