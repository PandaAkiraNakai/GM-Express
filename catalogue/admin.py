from django.contrib import admin
from .models import Categoria, Producto
from .forms import CategoriaForm, ProductoForm

class CategoriaAdmin(admin.ModelAdmin):
    form = CategoriaForm
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre']

class ProductoAdmin(admin.ModelAdmin):
    form = ProductoForm
    list_display = ['nombre', 'precio', 'stock', 'categoria_id']
    list_filter = ['categoria_id']
    search_fields = ['nombre']

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)