from django.contrib import admin
from .models import TipoUsuario, Usuario
from .forms import UsuarioForm, TipoUsuarioForm

class UsuarioAdmin(admin.ModelAdmin):
    form = UsuarioForm
    list_display = ['run', 'nombre', 'paterno', 'correo']
    search_fields = ['run', 'nombre', 'paterno', 'correo']
    
class TipoUsuarioAdmin(admin.ModelAdmin):
    form = TipoUsuarioForm
    list_display = ['descripcion']

admin.site.register(TipoUsuario, TipoUsuarioAdmin)
admin.site.register(Usuario, UsuarioAdmin)