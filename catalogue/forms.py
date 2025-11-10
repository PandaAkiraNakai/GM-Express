from django import forms
from django.core.exceptions import ValidationError
from .models import Categoria, Producto

class CategoriaForm(forms.ModelForm):
    """
    Formulario para crear y editar categorías de productos.
    Incluye validación para evitar nombres duplicados.
    """
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Almuerzos, Bebidas, Repostería'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción de la categoría',
                'rows': 3
            }),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre de la Categoría',
            'descripcion': 'Descripción',
            'estado': 'Estado',
        }
    
    def clean_nombre(self):
        """Valida que el nombre de categoría no esté duplicado"""
        nombre = self.cleaned_data.get('nombre')
        
        # Si estamos editando, excluir el registro actual
        if self.instance.pk:
            if Categoria.objects.filter(nombre__iexact=nombre).exclude(pk=self.instance.pk).exists():
                raise ValidationError('Ya existe una categoría con este nombre.')
        else:
            if Categoria.objects.filter(nombre__iexact=nombre).exists():
                raise ValidationError('Ya existe una categoría con este nombre.')
        
        return nombre


class ProductoForm(forms.ModelForm):
    """
    Formulario para crear y editar productos del catálogo.
    Incluye validaciones de negocio:
    - Precio mayor a 0
    - Stock no negativo
    - Categoría activa
    """
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'imagen', 'categoria_id']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del producto'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del producto',
                'rows': 3
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Precio en pesos chilenos',
                'min': 1
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cantidad disponible',
                'min': 0
            }),
            'imagen': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: producto.jpg (debe existir en static/images/)'
            }),
            'categoria_id': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre del Producto',
            'descripcion': 'Descripción',
            'precio': 'Precio (CLP)',
            'stock': 'Stock Disponible',
            'imagen': 'Nombre del Archivo de Imagen',
            'categoria_id': 'Categoría',
        }
    
    def clean_precio(self):
        """Valida que el precio sea mayor a 0"""
        precio = self.cleaned_data.get('precio')
        
        if precio <= 0:
            raise ValidationError('El precio debe ser mayor a 0.')
        
        if precio > 10000000:
            raise ValidationError('El precio no puede ser mayor a $10.000.000.')
        
        return precio
    
    def clean_stock(self):
        """Valida que el stock no sea negativo"""
        stock = self.cleaned_data.get('stock')
        
        if stock < 0:
            raise ValidationError('El stock no puede ser negativo.')
        
        return stock
    
    def clean_nombre(self):
        """Valida que el nombre del producto no esté duplicado en la misma categoría"""
        nombre = self.cleaned_data.get('nombre')
        
        # Validar duplicados
        if self.instance.pk:
            if Producto.objects.filter(nombre__iexact=nombre).exclude(pk=self.instance.pk).exists():
                raise ValidationError('Ya existe un producto con este nombre.')
        else:
            if Producto.objects.filter(nombre__iexact=nombre).exists():
                raise ValidationError('Ya existe un producto con este nombre.')
        
        return nombre
