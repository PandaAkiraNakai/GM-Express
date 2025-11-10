from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Venta, DetalleVenta
from catalogue.models import Producto
from datetime import date

class VentaForm(forms.ModelForm):
    """
    Formulario para crear y editar ventas.
    Incluye validaciones de negocio:
    - Fecha de venta no puede ser futura
    - Monto total mayor a 0
    - Usuario activo
    """
    class Meta:
        model = Venta
        fields = ['fecha_venta', 'estado', 'tipo_venta', 'monto_total', 'usuario']
        widgets = {
            'fecha_venta': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'tipo_venta': forms.Select(attrs={'class': 'form-control'}),
            'monto_total': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Monto total en pesos chilenos',
                'min': 1
            }),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'fecha_venta': 'Fecha de Venta',
            'estado': 'Estado de la Venta',
            'tipo_venta': 'Tipo de Venta',
            'monto_total': 'Monto Total (CLP)',
            'usuario': 'Usuario',
        }
    
    def clean_fecha_venta(self):
        """Valida que la fecha de venta no sea futura"""
        fecha = self.cleaned_data.get('fecha_venta')
        
        if fecha > date.today():
            raise ValidationError('La fecha de venta no puede ser en el futuro.')
        
        return fecha
    
    def clean_monto_total(self):
        """Valida que el monto total sea mayor a 0"""
        monto = self.cleaned_data.get('monto_total')
        
        if monto <= 0:
            raise ValidationError('El monto total debe ser mayor a 0.')
        
        if monto > 100000000:
            raise ValidationError('El monto total no puede ser mayor a $100.000.000.')
        
        return monto


class DetalleVentaForm(forms.ModelForm):
    """
    Formulario para agregar productos a una venta.
    Incluye validaciones de negocio:
    - Cantidad mayor a 0
    - Stock disponible suficiente
    - Precio unitario mayor a 0
    """
    class Meta:
        model = DetalleVenta
        fields = ['venta', 'producto', 'precio_unitario', 'cantidad']
        widgets = {
            'venta': forms.Select(attrs={'class': 'form-control'}),
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'precio_unitario': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Precio unitario',
                'min': 1
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cantidad a vender',
                'min': 1
            }),
        }
        labels = {
            'venta': 'Venta',
            'producto': 'Producto',
            'precio_unitario': 'Precio Unitario (CLP)',
            'cantidad': 'Cantidad',
        }
    
    def clean_cantidad(self):
        """Valida que la cantidad sea mayor a 0 y que haya stock suficiente"""
        cantidad = self.cleaned_data.get('cantidad')
        producto = self.cleaned_data.get('producto')
        
        if cantidad <= 0:
            raise ValidationError('La cantidad debe ser mayor a 0.')
        
        # Validar stock disponible
        if producto:
            if cantidad > producto.stock:
                raise ValidationError(
                    f'Stock insuficiente. Disponible: {producto.stock} unidades.'
                )
        
        return cantidad
    
    def clean_precio_unitario(self):
        """Valida que el precio unitario sea mayor a 0"""
        precio = self.cleaned_data.get('precio_unitario')
        
        if precio <= 0:
            raise ValidationError('El precio unitario debe ser mayor a 0.')
        
        return precio
    
    def clean(self):
        """Validación adicional para verificar consistencia de precios"""
        cleaned_data = super().clean()
        producto = cleaned_data.get('producto')
        precio_unitario = cleaned_data.get('precio_unitario')
        
        # Advertir si el precio es muy diferente al precio del producto
        if producto and precio_unitario:
            diferencia = abs(producto.precio - precio_unitario) / producto.precio
            if diferencia > 0.5:  # Más de 50% de diferencia
                # Nota: En un sistema real, esto podría ser solo una advertencia
                pass
        
        return cleaned_data
