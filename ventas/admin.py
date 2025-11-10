from django.contrib import admin
from .models import Venta, DetalleVenta
from .forms import VentaForm, DetalleVentaForm

class VentaAdmin(admin.ModelAdmin):
    form = VentaForm
    list_display = ['fecha_venta', 'usuario_id', 'tipo_venta']
    list_filter = ['tipo_venta', 'fecha_venta']

class DetalleVentaAdmin(admin.ModelAdmin):
    form = DetalleVentaForm
    list_display = ['venta_id', 'producto_id', 'cantidad', 'precio_unitario']

admin.site.register(Venta, VentaAdmin)
admin.site.register(DetalleVenta, DetalleVentaAdmin)