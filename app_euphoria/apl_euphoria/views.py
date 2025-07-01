from django.shortcuts import render
from django.http import HttpResponse
from apl_euphoria.models import *

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
def Clientes(request):
    clientes =  {
        'client': Cliente.objects.all()
        } 
    return render(request,'clientes.html', {'cliente': clientes})

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
def vista1(request):
    return HttpResponse("esta es mi primera vista")
#marca cosmeticos
def Marcacosmeticos(request):
    return render(request,'marcacosmeticos.html')

def vista2(request):
    persona = {
        'nombre': 'Edward',
        'edad': 30,
        'correo': 'edward@example.com'
    }
    return HttpResponse(persona)

def vista3(request):
    return render(request, 'index.html')
#Categoria
def Categoria(request):
    return render(request,'Categoria.html')