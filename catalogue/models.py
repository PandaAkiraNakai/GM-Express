from django.db import models
from django.utils import timezone
from catalogue.choices import estado

# modelos de la base de datos: tabla producto - servicio - categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    estado = models.CharField(max_length=1,choices=estado,default='1', verbose_name="Estado")
    descripcion = models.CharField(max_length=200, null=False)

    def __str__(self):
        return f"CATEGORÍA: {self.nombre}"

    class Meta:
        db_table = 'categoria'
        verbose_name ='Categoria'
        verbose_name_plural = 'Categorias'
        
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.PositiveIntegerField(null=False, verbose_name="Precio")
    stock = models.PositiveIntegerField(null=False, verbose_name="Stock")
    imagen = models.ImageField(upload_to='productos/', default='productos/default.jpg', verbose_name="Imagen")
    categoria_id = models.ForeignKey(Categoria, on_delete=models.PROTECT, limit_choices_to={'estado': '1'}, verbose_name="Categoría")
    def __str__(self):
        return f"ID: {self.id} | NOMBRE: {self.nombre} | DESCRIPCIÓN: {self.descripcion} | PRECIO: {self.precio} | STOCK: {self.stock} | IMAGEN: {self.imagen} | CATEGORÍA: {self.categoria_id}"

    class Meta:
        db_table = 'producto'
        verbose_name ='Producto'
        verbose_name_plural = 'Productos'