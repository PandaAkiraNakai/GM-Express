from catalogo.models import Servicio

# Limpiar servicios existentes
Servicio.objects.all().delete()
print("🧹 Servicios anteriores eliminados")

# Crear servicios de ejemplo
servicios = [
    Servicio(
        nombre='Catering Corporativo',
        descripcion='Servicios de alimentación para empresas, oficinas y eventos corporativos. Menús balanceados y nutritivos.',
        precio=15000.00,
        estado='1',
        servicio_tipo='catering-corporativo',
        imagen='catering.jpg'
    ),
    Servicio(
        nombre='Eventos y Banquetes',
        descripcion='Organización completa de eventos, matrimonios, celebraciones y banquetes con servicio integral.',
        precio=25000.00,
        estado='1',
        servicio_tipo='eventos-banquetes',
        imagen='eventos.jpg'
    ),
    Servicio(
        nombre='Delivery Empresarial',
        descripcion='Entrega de almuerzos y desayunos a empresas y oficinas. Servicio rápido y confiable.',
        precio=8000.00,
        estado='1',
        servicio_tipo='delivery-empresarial',
        imagen='delivery.jpg'
    ),
    Servicio(
        nombre='Catering para Colegios',
        descripcion='Alimentación escolar nutritiva y balanceada. Menús supervisados por nutricionistas.',
        precio=3500.00,
        estado='1',
        servicio_tipo='catering-colegios',
        imagen='colegio.jpg'
    ),
    Servicio(
        nombre='Servicios VIP',
        descripcion='Servicios exclusivos para eventos especiales, con atención personalizada y menús gourmet.',
        precio=45000.00,
        estado='1',
        servicio_tipo='servicios-vip',
        imagen='vip.jpg'
    ),
    Servicio(
        nombre='Catering Hospitalario',
        descripcion='Alimentación especializada para centros de salud, con dietas terapéuticas y supervisión nutricional.',
        precio=12000.00,
        estado='1',
        servicio_tipo='catering-hospitalario',
        imagen='hospital.jpg'
    )
]

# Guardar en la base de datos
for servicio in servicios:
    servicio.save()
    print(f"✅ {servicio.nombre} - ${servicio.precio:,.0f}")

print(f"\n🎉 Total servicios creados: {Servicio.objects.count()}")
print(f"🟢 Servicios activos: {Servicio.objects.filter(estado='1').count()}")