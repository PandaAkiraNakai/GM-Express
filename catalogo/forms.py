from django import forms
from django.core.exceptions import ValidationError
from .models import Servicio, Categoria, Producto

class ServicioForm(forms.ModelForm):
    """
    Formulario para crear y editar servicios de GM-Express.
    Incluye validación para evitar tipos de servicio duplicados.
    """
    class Meta:
        model = Servicio
        fields = ['nombre', 'imagen', 'servicio_tipo', 'descripcion', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Catering Corporativo'
            }),
            'imagen': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: catering.jpg (debe existir en static/images/)'
            }),
            'servicio_tipo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: catering-corporativo (sin espacios, minúsculas)'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del servicio',
                'rows': 3
            }),
            'estado': forms.Select(attrs={
                'class': 'form-control',
                'choices': [('1', 'Activo'), ('0', 'Inactivo')]
            }),
        }
        labels = {
            'nombre': 'Nombre del Servicio',
            'imagen': 'Nombre del Archivo de Imagen',
            'servicio_tipo': 'Tipo de Servicio (slug)',
            'descripcion': 'Descripción',
            'estado': 'Estado',
        }
    
    def clean_servicio_tipo(self):
        """
        Valida que el servicio_tipo no esté duplicado y tenga formato correcto.
        Debe ser en minúsculas, sin espacios, separado por guiones.
        """
        servicio_tipo = self.cleaned_data.get('servicio_tipo')
        
        # Validar formato
        import re
        if not re.match(r'^[a-z0-9-]+$', servicio_tipo):
            raise ValidationError(
                'El tipo de servicio debe estar en minúsculas, sin espacios. '
                'Use guiones para separar palabras. Ej: catering-corporativo'
            )
        
        # Validar duplicados
        if self.instance.pk:
            if Servicio.objects.filter(servicio_tipo=servicio_tipo).exclude(pk=self.instance.pk).exists():
                raise ValidationError('Ya existe un servicio con este tipo.')
        else:
            if Servicio.objects.filter(servicio_tipo=servicio_tipo).exists():
                raise ValidationError('Ya existe un servicio con este tipo.')
        
        return servicio_tipo
    
    def clean_nombre(self):
        """Valida que el nombre del servicio no esté duplicado"""
        nombre = self.cleaned_data.get('nombre')
        
        if self.instance.pk:
            if Servicio.objects.filter(nombre__iexact=nombre).exclude(pk=self.instance.pk).exists():
                raise ValidationError('Ya existe un servicio con este nombre.')
        else:
            if Servicio.objects.filter(nombre__iexact=nombre).exists():
                raise ValidationError('Ya existe un servicio con este nombre.')
        
        return nombre


class CategoriaWebForm(forms.ModelForm):
    """
    Formulario para crear y editar categorías del catálogo web.
    """
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la categoría'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción de la categoría',
                'rows': 3
            }),
            'estado': forms.Select(attrs={
                'class': 'form-control',
                'choices': [('1', 'Activo'), ('0', 'Inactivo')]
            }),
        }
        labels = {
            'nombre': 'Nombre de la Categoría',
            'descripcion': 'Descripción',
            'estado': 'Estado',
        }
    
    def clean_nombre(self):
        """Valida que el nombre no esté duplicado"""
        nombre = self.cleaned_data.get('nombre')
        
        if self.instance.pk:
            if Categoria.objects.filter(nombre__iexact=nombre).exclude(pk=self.instance.pk).exists():
                raise ValidationError('Ya existe una categoría con este nombre.')
        else:
            if Categoria.objects.filter(nombre__iexact=nombre).exists():
                raise ValidationError('Ya existe una categoría con este nombre.')
        
        return nombre


class ProductoWebForm(forms.ModelForm):
    """
    Formulario para crear y editar productos del catálogo web.
    """
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'categoria', 'servicio']
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
            'imagen': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: producto.jpg'
            }),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'servicio': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre del Producto',
            'descripcion': 'Descripción',
            'precio': 'Precio (CLP)',
            'imagen': 'Nombre del Archivo de Imagen',
            'categoria': 'Categoría',
            'servicio': 'Servicio',
        }
    
    def clean_precio(self):
        """Valida que el precio sea mayor a 0"""
        precio = self.cleaned_data.get('precio')
        
        if precio <= 0:
            raise ValidationError('El precio debe ser mayor a 0.')
        
        if precio > 10000000:
            raise ValidationError('El precio no puede ser mayor a $10.000.000.')
        
        return precio
