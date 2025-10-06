#!/usr/bin/env python
"""
Script para poblar la base de datos con servicios de GM-Express
"""
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gmexpress.settings')
django.setup()

from catalogo.models import Servicio

def crear_servicios():
    """Crear servicios de ejemplo para GM-Express"""
    
    servicios_data = [
        {
            'nombre': 'Catering Corporativo',
            'descripcion': 'Servicios de alimentación para empresas, oficinas y eventos corporativos. Menús balanceados y nutritivos.',
            'precio': 15000.00,
            'estado': '1',
            'servicio_tipo': 'catering-corporativo',
            'imagen': 'catering.jpg'
        },
        {
            'nombre': 'Eventos y Banquetes',
            'descripcion': 'Organización completa de eventos, matrimonios, celebraciones y banquetes con servicio integral.',
            'precio': 25000.00,
            'estado': '1',
            'servicio_tipo': 'eventos-banquetes',
            'imagen': 'eventos.jpg'
        },
        {
            'nombre': 'Delivery Empresarial',
            'descripcion': 'Entrega de almuerzos y desayunos a empresas y oficinas. Servicio rápido y confiable.',
            'precio': 8000.00,
            'estado': '1',
            'servicio_tipo': 'delivery-empresarial',
            'imagen': 'delivery.jpg'
        },
        {
            'nombre': 'Catering para Colegios',
            'descripcion': 'Alimentación escolar nutritiva y balanceada. Menús supervisados por nutricionistas.',
            'precio': 3500.00,
            'estado': '1',
            'servicio_tipo': 'catering-colegios',
            'imagen': 'colegio.jpg'
        },
        {
            'nombre': 'Servicios VIP',
            'descripcion': 'Servicios exclusivos para eventos especiales, con atención personalizada y menús gourmet.',
            'precio': 45000.00,
            'estado': '1',
            'servicio_tipo': 'servicios-vip',
            'imagen': 'vip.jpg'
        },
        {
            'nombre': 'Catering Hospitalario',
            'descripcion': 'Alimentación especializada para centros de salud, con dietas terapéuticas y supervisión nutricional.',
            'precio': 12000.00,
            'estado': '1',
            'servicio_tipo': 'catering-hospitalario',
            'imagen': 'hospital.jpg'
        }
    ]
    
    print("🍽️ CREANDO SERVICIOS GM-EXPRESS")
    print("="*40)
    
    # Limpiar servicios existentes
    Servicio.objects.all().delete()
    print("🧹 Servicios anteriores eliminados")
    
    # Crear nuevos servicios
    servicios_creados = 0
    for servicio_data in servicios_data:
        servicio, created = Servicio.objects.get_or_create(
            servicio_tipo=servicio_data['servicio_tipo'],
            defaults=servicio_data
        )
        if created:
            servicios_creados += 1
            print(f"✅ {servicio.nombre} - ${servicio.precio:,.0f}")
        else:
            print(f"⚠️  {servicio.nombre} ya existía")
    
    print(f"\n🎉 {servicios_creados} servicios creados exitosamente")
    print(f"📊 Total servicios en BD: {Servicio.objects.count()}")
    
    # Verificar servicios activos
    servicios_activos = Servicio.objects.filter(estado='1')
    print(f"🟢 Servicios activos: {servicios_activos.count()}")

if __name__ == '__main__':
    crear_servicios()