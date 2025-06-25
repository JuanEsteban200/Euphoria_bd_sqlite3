from django.shortcuts import render

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