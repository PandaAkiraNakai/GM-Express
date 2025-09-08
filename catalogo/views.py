from django.shortcuts import render
from catalogo import models as datos
# Create your views here.
def catalogoServicios(request):
    data = {
        'catalogo_servicios': datos.catalogoprincipal,
    }
    return render(request, 'templateEmpresa/inicio.html', data)

def catalogoProductos(request, servicio_tipo):
    # Mapeo de tipos de servicio a sus respectivos catálogos
    servicios_map = {
        'transportado': datos.catalogo_transporte,
        'coffee': datos.catalogo_eventos,
        'tradicional': datos.catalogo_presencial,
        'reposteria': datos.catalogo_snacks,
        'concesion': datos.catalogo_servicios,
    }
    # Nombres para mostrar en el template
    nombres_servicios = {
    'transportado': 'Wraps, ensaladas y platos internacionales',
    'coffee': 'Canapés, quiches y dulces para eventos',
    'tradicional': 'Risottos, pastas y cocina internacional',
    'reposteria': 'Snacks saludables y repostería creativa',
    'concesion': 'Servicios Empresariales',
    }
    if servicio_tipo in servicios_map:
        data = {
            'catalogo_productos': servicios_map[servicio_tipo],
            'titulo_servicio': nombres_servicios[servicio_tipo],
            'servicio_tipo': servicio_tipo,
        }
        return render(request, 'templateCatalogo/catalogo2.html', data)
    else:
        # Si el servicio no existe, redirigir al catálogo principal
        return catalogoServicios(request)

def catalogoMenu(request, servicio_tipo, producto_id):
    # Mapeo de tipos de servicio a sus respectivos menús
    menus_map = {
        'transportado': datos.menu_transporte,
        'coffee': datos.menu_eventos,
        'tradicional': datos.menu_presencial,
        'reposteria': datos.menu_snacks,
        'concesion': datos.menu_servicios,
    }
    # Mapeo de nombres de productos
    productos_map = {
        'transportado': datos.catalogo_transporte,
        'coffee': datos.catalogo_eventos,
        'tradicional': datos.catalogo_presencial,
        'reposteria': datos.catalogo_snacks,
        'concesion': datos.catalogo_servicios,
    }
    if servicio_tipo in menus_map and int(producto_id) in menus_map[servicio_tipo]:
        menu_item = menus_map[servicio_tipo][int(producto_id)]
        producto_info = productos_map[servicio_tipo][int(producto_id)]
        data = {
            'menu_detalle': menu_item,
            'producto_nombre': producto_info['nombre'],
            'producto_imagen': producto_info['imagen'],
            'servicio_tipo': servicio_tipo,
        }
        return render(request, 'templateCatalogo/catalogo3.html', data)