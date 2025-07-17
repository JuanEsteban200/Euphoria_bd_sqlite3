from django.db import models

# Create your models here.

class Administrador(models.Model):
    id_administrador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    numero_telefono = models.CharField(max_length=20)
    Indexes = models.Index(fields=['id_cliente'])
    def __str__(self):
        return self.nombre

class Vendedor(models.Model):
    id_vendedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    Indexes = models.Index(fields=['id_vendedor'])
    
class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_vendedor = models.ForeignKey('Vendedor', on_delete=models.CASCADE)
    detalles = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    cantidad = models.IntegerField()
    id_administrador = models.ForeignKey('Administrador', on_delete=models.CASCADE)
    id_pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.ForeignKey('CategoriaProducto', on_delete=models.CASCADE)
    marca = models.ForeignKey('MarcaCosmetico', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class Pedido(models.Model): 
    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField()

class DetallePedido(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    metodo_pago = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    confirmacion_pago = models.TextField()

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=100)

class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_compra = models.DateField()
    id_administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)

class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    numero = models.CharField(max_length=100)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Promocion(models.Model):
    id_promocion = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    requisitos = models.TextField()
    rendimiento = models.TextField()

class CategoriaProducto(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre
    
class MarcaCosmetico(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    detalles = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidades = models.IntegerField()
    
    def __str__(self):
        return self.nombre


class Pqr(models.Model):
    id_pqr = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    direccion_cliente = models.CharField(max_length=255)
    telefono_cliente = models.CharField(max_length=20)
    descripcion = models.TextField()
    id_administrador = models.ForeignKey('Administrador', on_delete=models.CASCADE)
    
