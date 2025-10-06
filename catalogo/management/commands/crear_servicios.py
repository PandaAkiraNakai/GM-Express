from django.core.management.base import BaseCommand
from catalogo.models import Servicio

class Command(BaseCommand):
    help = 'Crear servicios de ejemplo para GM-Express'

    def handle(self, *args, **options):
        self.stdout.write("🍽️ VERIFICANDO SERVICIOS GM-EXPRESS")
        self.stdout.write("="*40)
        
        # Verificar servicios existentes
        servicios_existentes = Servicio.objects.all()
        self.stdout.write(f"📊 Servicios existentes: {servicios_existentes.count()}")
        
        for servicio in servicios_existentes:
            self.stdout.write(f"✅ {servicio.nombre} - Estado: {servicio.estado}")
        
        # Verificar servicios activos
        servicios_activos = Servicio.objects.filter(estado='1')
        self.stdout.write(f"\n🟢 Servicios activos: {servicios_activos.count()}")
        
        if servicios_activos.count() == 0:
            self.stdout.write("⚠️ No hay servicios activos. Activando servicios existentes...")
            Servicio.objects.all().update(estado='1')
            self.stdout.write("✅ Todos los servicios han sido activados")
        
        self.stdout.write(
            self.style.SUCCESS('\n¡Servicios verificados! Recarga la página para verlos.')
        )