from django.http import HttpResponse

from django.shortcuts import render
from catalogo import models as datos

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
    data = {
        'catalogo_servicios': datos.catalogoprincipal,
    }
    return render(request, 'templateEmpresa/inicio.html', data)