from django.db import models

# Create your models here.

TIPO_CHOICES = [
    ('E', 'Entrada'),
    ('S', 'Salida'),
    ('T', 'Traslado'),
    ('P', 'Proveedores'),
]

class Almacen(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=20)
    
    def __str__(self):
        return f'cod: {self.codigo} - {self.nombre}'

class Producto(models.Model):
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=20)
    umed = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.codigo

class TipoMoinventario(models.Model):
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.codigo} - {self.descripcion}'

class MovimientoInventario(models.Model):
    fecha = models.DateField(default=None)
    tipo = models.ForeignKey(TipoMoinventario, on_delete=models.CASCADE)
    documento = models.CharField(max_length=20)
    almacen_afectado = models.ForeignKey(Almacen, on_delete=models.CASCADE, related_name='almacen_afectado')
    almacen_destino = models.ForeignKey(Almacen, on_delete=models.CASCADE, related_name='almacen_destino')
    nit = models.CharField(max_length=20)
    sucursal = models.CharField(max_length=20)
    orden_no = models.CharField(max_length=20)
    transporte = models.CharField(max_length=20)
    nota_1 = models.CharField(max_length=20, blank=True)
    nota_2 = models.CharField(max_length=20, blank=True)
    nota_3 = models.CharField(max_length=20, blank=True)
    
    productos = models.ManyToManyField(Producto, through='MovimientoInventarioProducto')
    
    def __str__(self):
        return self.documento
    
    class Meta:
        verbose_name_plural = "Movimientos de Inventario"
        ordering = ['-fecha', 'documento']
    
class MovimientoInventarioProducto(models.Model):
    movimiento_inventario = models.ForeignKey(MovimientoInventario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=20)
    umed = models.CharField(max_length=4)
    cantidad = models.IntegerField(default=1)
    costo_unit = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.producto.codigo
    