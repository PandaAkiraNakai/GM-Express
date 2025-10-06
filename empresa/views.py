from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from catalogo.models import Servicio
from catalogue.models import Categoria, Producto
from usuarios.models import Usuario, TipoUsuario
from ventas.models import Venta, DetalleVenta

def info_empresa(request): 
    datos = {
        'historia': "GM-Express empresa chilena de Servicios de Alimentación, formada por un equipo de profesionales 100% comprometidos que día a día trabaja orientando sus acciones para asegurar y promover el bienestar nutricional mejorando la experiencia y calidad de vida de sus clientes. Ofrecemos soluciones personalizadas y rápida capacidad de respuesta a la mejor relación Precio | Calidad del mercado. Para GM-Express tú eres lo más importante.",
        'mision': "Más que un servicio de alimentación, queremos entregar confianza y la mejor experiencia a nuestros clientes para contribuir a sus objetivos, ser siempre relevantes en sus vidas y establecer relaciones perdurables esforzándonos día a día para entregar un servicio integral, amable y oportuno de manera sostenible.",
        'vision': "Consolidarnos como una empresa de alimentación sostenible y de excelencia en la región, reconocida por superar y entregar la mejor experiencia a sus clientes, con productos y servicios de alta calidad y confiabilidad.",
        'valores': ["Compromiso", "Calidad", "Trabajo en equipo","Pasión por el servicio", "Sustentabilidad","Lealtad"],
        'contactos': {
            'teléfono': "+569 7615 9518 / +569 4785 4598",
            'email': "ventas@gmexpress.cl / proveedores@gmexpress.cl"
        },
        'redes': [
            {'nombre': "Facebook", 'url': "https://www.facebook.com/GMEXPRESSCL"},
            {'nombre': "Instagram", 'url': "https://www.instagram.com/gmexpress_cl/?hl=es"},
        ]
    }
    # Comentario: renderiza la plantilla y pasa el diccionario 'datos'
    return render(request, 'templateEmpresa/info.html', datos)


def inicio(request):
    catalogo_servicios = Servicio.objects.filter(estado='1')
    data = {
        'catalogo_servicios': catalogo_servicios,
    }
    return render(request, 'templateEmpresa/inicio.html', data)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'templateEmpresa/login.html')

@login_required
def dashboard(request):
    # Estadísticas para el dashboard
    total_usuarios = Usuario.objects.count()
    total_productos = Producto.objects.count()
    total_categorias = Categoria.objects.count()
    total_servicios = Servicio.objects.count()
    total_ventas = Venta.objects.count()
    
    # Ventas recientes
    ventas_recientes = Venta.objects.order_by('-fecha_venta')[:5]
    
    context = {
        'total_usuarios': total_usuarios,
        'total_productos': total_productos,
        'total_categorias': total_categorias,
        'total_servicios': total_servicios,
        'total_ventas': total_ventas,
        'ventas_recientes': ventas_recientes,
    }
    return render(request, 'templateEmpresa/dashboard.html', context)

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente')
    return redirect('inicio')