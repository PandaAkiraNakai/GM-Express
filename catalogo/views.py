
from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto, Servicio

# Vista para mostrar el catálogo principal de servicios
def catalogoServicios(request):
    # Obtener todos los servicios activos
    catalogo_servicios = Servicio.objects.filter(estado='1')
    data = {
        'catalogo_servicios': catalogo_servicios,
    }
    return render(request, 'templateEmpresa/inicio.html', data)


# Vista para mostrar productos de una categoría/servicio
def catalogoProductos(request, servicio_tipo):
    # Buscar el servicio por tipo
    try:
        servicio = Servicio.objects.get(servicio_tipo=servicio_tipo, estado='1')
        # Obtener productos relacionados a ese servicio
        productos = Producto.objects.filter(servicio=servicio)
        data = {
            'catalogo_productos': productos,
            'titulo_servicio': servicio.nombre,
            'servicio_tipo': servicio_tipo,
        }
        return render(request, 'templateCatalogo/catalogo2.html', data)
    except Servicio.DoesNotExist:
        # Si el servicio no existe, redirigir al catálogo principal
        return catalogoServicios(request)


# Vista para mostrar el detalle de un producto
def catalogoMenu(request, servicio_tipo, producto_id):
    try:
        producto = get_object_or_404(Producto, pk=producto_id)
        servicio = get_object_or_404(Servicio, servicio_tipo=servicio_tipo, estado='1')
        
        data = {
            'menu_detalle': producto,
            'producto_nombre': producto.nombre,
            'producto_imagen': producto.imagen,
            'servicio_tipo': servicio_tipo,
        }
        return render(request, 'templateCatalogo/catalogo3.html', data)
    except (Producto.DoesNotExist, Servicio.DoesNotExist):
        # Si no existe el producto o servicio, redirigir al catálogo
        return catalogoServicios(request)