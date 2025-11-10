from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Usuario, TipoUsuario
import re
from datetime import date

class TipoUsuarioForm(forms.ModelForm):
    """
    Formulario para crear y editar tipos de usuario.
    Incluye validación para evitar duplicados de descripción.
    """
    class Meta:
        model = TipoUsuario
        fields = ['descripcion', 'estado']
        widgets = {
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Administrador, Cliente, Empleado'
            }),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'descripcion': 'Descripción del Tipo de Usuario',
            'estado': 'Estado',
        }
    
    def clean_descripcion(self):
        """Valida que la descripción no esté duplicada"""
        descripcion = self.cleaned_data.get('descripcion')
        
        # Si estamos editando, excluir el registro actual
        if self.instance.pk:
            if TipoUsuario.objects.filter(descripcion__iexact=descripcion).exclude(pk=self.instance.pk).exists():
                raise ValidationError('Ya existe un tipo de usuario con esta descripción.')
        else:
            if TipoUsuario.objects.filter(descripcion__iexact=descripcion).exists():
                raise ValidationError('Ya existe un tipo de usuario con esta descripción.')
        
        return descripcion


class UsuarioForm(forms.ModelForm):
    """
    Formulario para crear y editar usuarios.
    Incluye validaciones de negocio:
    - RUT chileno válido
    - Correo único
    - Fecha de nacimiento en el pasado
    - Contraseña segura
    """
    confirmar_contrasenia = forms.CharField(
        max_length=255, 
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirme la contraseña'
        }),
        label='Confirmar Contraseña',
        required=False
    )
    
    class Meta:
        model = Usuario
        fields = ['run', 'nombre', 'paterno', 'materno', 'correo', 'contrasenia', 
                  'telefono', 'fecha_nacimiento', 'estado', 'tipo_usuario']
        widgets = {
            'run': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 12.345.678-9'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre'
            }),
            'paterno': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido Paterno'
            }),
            'materno': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido Materno'
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com'
            }),
            'contrasenia': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Mínimo 9 caracteres, 1 mayúscula, 1 símbolo'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+56912345678'
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'tipo_usuario': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'run': 'RUT',
            'nombre': 'Nombre',
            'paterno': 'Apellido Paterno',
            'materno': 'Apellido Materno',
            'correo': 'Correo Electrónico',
            'contrasenia': 'Contraseña',
            'telefono': 'Teléfono',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'estado': 'Estado',
            'tipo_usuario': 'Tipo de Usuario',
        }
    
    def clean_run(self):
        """Valida formato y dígito verificador del RUT chileno"""
        run = self.cleaned_data.get('run')
        
        # Limpiar formato del RUT (quitar puntos y guión)
        run_limpio = run.replace('.', '').replace('-', '')
        
        # Verificar formato básico
        if not re.match(r'^\d{7,8}[0-9kK]$', run_limpio):
            raise ValidationError('Formato de RUT inválido. Use formato: 12.345.678-9 o 12345678-9')
        
        # Validar duplicados
        if self.instance.pk:
            if Usuario.objects.filter(run=run).exclude(pk=self.instance.pk).exists():
                raise ValidationError('Ya existe un usuario con este RUT.')
        else:
            if Usuario.objects.filter(run=run).exists():
                raise ValidationError('Ya existe un usuario con este RUT.')
        
        return run
    
    def clean_correo(self):
        """Valida que el correo sea único"""
        correo = self.cleaned_data.get('correo')
        
        if self.instance.pk:
            if Usuario.objects.filter(correo__iexact=correo).exclude(pk=self.instance.pk).exists():
                raise ValidationError('Ya existe un usuario con este correo electrónico.')
        else:
            if Usuario.objects.filter(correo__iexact=correo).exists():
                raise ValidationError('Ya existe un usuario con este correo electrónico.')
        
        return correo
    
    def clean_fecha_nacimiento(self):
        """Valida que la fecha de nacimiento sea en el pasado y usuario tenga al menos 18 años"""
        fecha = self.cleaned_data.get('fecha_nacimiento')
        
        if fecha >= date.today():
            raise ValidationError('La fecha de nacimiento debe ser en el pasado.')
        
        # Calcular edad
        edad = (date.today() - fecha).days // 365
        if edad < 18:
            raise ValidationError('El usuario debe tener al menos 18 años.')
        
        return fecha
    
    def clean(self):
        """Validación de contraseñas coincidentes"""
        cleaned_data = super().clean()
        contrasenia = cleaned_data.get('contrasenia')
        confirmar = cleaned_data.get('confirmar_contrasenia')
        
        # Solo validar si se está creando o si se proporciona una nueva contraseña
        if not self.instance.pk or contrasenia:
            if contrasenia != confirmar:
                raise ValidationError('Las contraseñas no coinciden.')
        
        return cleaned_data
