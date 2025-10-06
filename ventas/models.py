from django.db import models
from django.utils import timezone
from ventas.choices import estado, tipo_venta
from catalogue.models import Producto
from usuarios.models import Usuario
# Create your models here.


class Venta(models.Model):
    fecha_venta = models.DateField(default=timezone.now, verbose_name="Fecha de Venta")
    estado = models.CharField(max_length=1, choices=estado, default='1', verbose_name="Estado")
    tipo_venta = models.CharField(max_length=1, choices=tipo_venta, default='p', verbose_name="Tipo de Venta")
    monto_total = models.PositiveIntegerField(null=False, verbose_name="Monto Total")
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, limit_choices_to={'estado': '1'}, verbose_name="Usuario")
    
    class Meta:
        db_table = "ventas"
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
    
    def __str__(self):
        return f"VENTA {self.id} | FECHA: {self.fecha_venta} | TOTAL: {self.monto_total} | ESTADO: {self.estado}"


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles', verbose_name="Venta")
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, verbose_name="Producto", null=True, blank=True)
    precio_unitario = models.PositiveIntegerField(null=False, verbose_name="Precio Unitario")
    cantidad = models.PositiveIntegerField(null=False, verbose_name="Cantidad")

    class Meta:
        db_table = "detalle_ventas"
        verbose_name = "Detalle Venta"
        verbose_name_plural = "Detalles Ventas"
        
    def __str__(self):
            return f"Venta #{self.venta.id} | Producto: {self.producto.nombre} | Cantidad: {self.cantidad} | Subtotal: {self.calcular_subtotal_producto()}"

    def calcular_subtotal_producto(self):
        self.subtotal = self.precio_unitario * self.cantidad
        return self.subtotal