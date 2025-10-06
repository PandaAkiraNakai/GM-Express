from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from usuarios.choices import estado

# Create your models here.

class TipoUsuario(models.Model):
    descripcion = models.CharField(max_length=45)
    estado = models.CharField(max_length=1, choices=estado, default='1')
    fecha_creacion = models.DateTimeField(default=timezone.now)
        
    def __str__(self):
        return f"CATEGORIA: {self.descripcion}"
    
    class Meta:
        db_table = 'tipo_usuario'
        verbose_name = "Tipo Usuario"
        verbose_name_plural = "tipos Usuarios"
        
class Usuario(models.Model):
    run = models.CharField(max_length=12, unique=True, null=False, verbose_name="RUT")
    nombre = models.CharField(max_length=45, null=False, blank=False, verbose_name="Nombre")
    paterno = models.CharField(max_length=45, null=False, blank=False, verbose_name="Apellido Paterno")
    materno = models.CharField(max_length=45, null=False, blank=False, verbose_name="Apellido Materno")
    correo = models.EmailField(max_length=100, unique=True, null=False, verbose_name="Correo Electrónico")
    contrasenia = models.CharField(max_length=255, validators=[RegexValidator(r'^(?=.*[A-Z])(?=.*[^A-Za-z0-9]).{9,}$', message="Debe tener al menos 9 caracteres, una mayúscula y un símbolo especial.")])
    telefono = models.CharField(max_length=15, null=False, blank=False, verbose_name="Teléfono")
    fecha_nacimiento = models.DateField(null=False, blank=False, verbose_name="Fecha de Nacimiento")
    fecha_registro = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Registro")
    estado = models.CharField(max_length=1,choices=estado,default='1', verbose_name="Estado")
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.PROTECT, limit_choices_to={'estado': '1'})
    
    class Meta:
        db_table = 'usuario'
        verbose_name = "Usuario"
        verbose_name_plural = "usuarios"
        
    def __str__(self):
        return f"{self.nombre} {self.paterno} {self.materno} - {self.correo}"
    
    def nombre_completo(self):
        return f"{self.nombre} {self.paterno} {self.materno}"