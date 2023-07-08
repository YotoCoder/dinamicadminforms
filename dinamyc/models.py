from django.db import models

class Almacen(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre

class TipoMovimiento(models.Model):
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre

class MovimientoInventario(models.Model):
    tipo = models.ForeignKey(TipoMovimiento, on_delete=models.CASCADE)
    
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)

    cantidad = models.IntegerField()
    
    def __str__(self):
        return f'{self.tipo} {self.cantidad} {self.almacen}'