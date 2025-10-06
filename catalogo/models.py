from django.db import models
from django.utils import timezone

# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    imagen = models.CharField(max_length=255, default='default.jpg')
    servicio_tipo = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=1, default='1')
    
    def __str__(self):
        return f"SERVICIO: {self.nombre}"
    
    class Meta:
        db_table = 'servicio'
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=200, null=False)
    estado = models.CharField(max_length=1, default='1')

    def __str__(self):
        return f"CATEGORÍA: {self.nombre}"

    class Meta:
        db_table = 'categoria_catalogo'
        verbose_name ='Categoria'
        verbose_name_plural = 'Categorias'
        
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.PositiveIntegerField(null=False, verbose_name="Precio")
    imagen = models.CharField(max_length=255, default='default.jpg')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, verbose_name="Categoría")
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT, verbose_name="Servicio", null=True, blank=True)
    
    def __str__(self):
        return f"ID: {self.id} | NOMBRE: {self.nombre} | PRECIO: {self.precio}"

    class Meta:
        db_table = 'producto_catalogo'
        verbose_name ='Producto'
        verbose_name_plural = 'Productos'