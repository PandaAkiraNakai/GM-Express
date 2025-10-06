from django.core.management.base import BaseCommand
from catalogo.models import Servicio, Producto

class Command(BaseCommand):
    help = 'Actualizar imágenes de servicios y productos con archivos existentes'

    def handle(self, *args, **options):
        self.stdout.write("🖼️ ACTUALIZANDO IMÁGENES")
        self.stdout.write("="*30)
        
        # Mapeo de servicios a imágenes existentes
        servicios_imagenes = {
            'transportado': 'transporte.png',
            'tradicional': 'presencial.png', 
            'concesion': 'servicio.png',
            'coffee': 'snack.png',
            'reposteria': 'tarta1.png',
            'Domicilio': 'gm express.png'
        }
        
        # Actualizar servicios
        self.stdout.write("📋 Actualizando servicios...")
        for servicio in Servicio.objects.all():
            if servicio.servicio_tipo in servicios_imagenes:
                nueva_imagen = servicios_imagenes[servicio.servicio_tipo]
                servicio.imagen = nueva_imagen
                servicio.save()
                self.stdout.write(f"✅ {servicio.nombre} -> {nueva_imagen}")
        
        # Mapeo de productos a imágenes (algunos ejemplos)
        productos_imagenes = {
            'almuerzo': 'Pasta al pesto.png',
            'vegetariano': 'ensalada mediterranea.png',
            'vegano': 'couscous vegetal.png',
            'sandwich': 'wrap de salmon.png',
            'jugo': 'Mix de frutos secos.png',
            'menu': 'Risotto de champiñones.png',
            'pollo': 'teriyaki.png',
            'lasagna': 'Tortilla española.png',
            'bowl': 'Omelette de espárragos.png',
            'filete': 'canapes de camaron.png',
            'pastel': 'quiches.png',
            'empanada': 'Brochetas caprese.png',
            'lomo': 'Sopa de tomate y albahaca.png',
            'ensalada': 'ensalada mediterranea.png',
            'desayuno': 'Chips de manzana.png',
            'crema': 'Sopa de tomate y albahaca.png',
            'cazuela': 'Pasta al pesto.png',
            'queque': 'tarta1.png',
            'torta': 'Tartaleta de limón.png',
            'galleta': 'Galletas de zanahoria.png',
            'brownie': 'Brownies de batata.png',
            'muffin': 'Trufas de chocolate.png',
        }
        
        # Actualizar productos
        self.stdout.write("\n🍽️ Actualizando productos...")
        productos_actualizados = 0
        for producto in Producto.objects.all():
            nombre_lower = producto.nombre.lower()
            imagen_asignada = None
            
            # Buscar coincidencias en el nombre
            for palabra_clave, imagen in productos_imagenes.items():
                if palabra_clave in nombre_lower:
                    producto.imagen = imagen
                    producto.save()
                    imagen_asignada = imagen
                    productos_actualizados += 1
                    break
            
            if imagen_asignada:
                self.stdout.write(f"✅ {producto.nombre} -> {imagen_asignada}")
            else:
                # Asignar imagen por defecto
                producto.imagen = 'servicio.png'
                producto.save()
                productos_actualizados += 1
                self.stdout.write(f"⚡ {producto.nombre} -> servicio.png (por defecto)")
        
        self.stdout.write(f"\n🎉 Actualización completa:")
        self.stdout.write(f"   📋 Servicios: {Servicio.objects.count()}")
        self.stdout.write(f"   🍽️ Productos: {productos_actualizados}")
        self.stdout.write(f"   🖼️ Imágenes asignadas correctamente")
        
        self.stdout.write(
            self.style.SUCCESS('\n¡Imágenes actualizadas! Recarga la página para verlas.')
        )