#!/bin/bash

# Script para migrar GM-Express a MySQL/XAMPP
echo "🚀 MIGRACIÓN GM-EXPRESS A MYSQL/XAMPP"
echo "======================================"

# Activar entorno virtual
echo "📦 Activando entorno virtual..."
source venv/bin/activate

# Verificar conexión con MySQL
echo "🔗 Verificando conexión con MySQL..."
python3 -c "
import pymysql
try:
    connection = pymysql.connect(host='localhost', user='root', password='', port=3306)
    print('✅ Conexión exitosa con MySQL')
    connection.close()
except Exception as e:
    print(f'❌ Error de conexión: {e}')
    print('💡 Asegúrate de que XAMPP esté ejecutándose')
    exit(1)
"

# Crear base de datos si no existe
echo "🗄️ Creando base de datos gmexpress..."
python3 -c "
import pymysql
connection = pymysql.connect(host='localhost', user='root', password='', port=3306)
cursor = connection.cursor()
try:
    cursor.execute('CREATE DATABASE IF NOT EXISTS gmexpress CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci')
    print('✅ Base de datos gmexpress creada/verificada')
except Exception as e:
    print(f'⚠️ Error: {e}')
finally:
    connection.close()
"

# Crear migraciones
echo "📋 Creando migraciones..."
python3 manage.py makemigrations

# Aplicar migraciones
echo "⚙️ Aplicando migraciones..."
python3 manage.py migrate

# Crear superusuario
echo "👤 Creando superusuario..."
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@gmexpress.cl', 'admin123') if not User.objects.filter(username='admin').exists() else print('Superusuario ya existe')" | python3 manage.py shell

# Migrar todos los datos
echo "📊 Migrando datos completos..."
python3 manage.py shell -c "
# Importar todos los modelos
from catalogo.models import Servicio, Categoria, Producto
from catalogue.models import Categoria as CatalogueCat, Producto as CatalogueProduct
from usuarios.models import TipoUsuario, Usuario
from ventas.models import Venta, DetalleVenta

print('🧹 Limpiando datos existentes...')
Servicio.objects.all().delete()
Categoria.objects.all().delete()
Producto.objects.all().delete()

print('🏷️ Creando servicios...')
servicios_data = [
    {'nombre': 'Alimentación transportada', 'imagen': 'transporte.jpg', 'servicio_tipo': 'transportado', 'descripcion': 'Servicio de alimentación con entrega a domicilio y empresas'},
    {'nombre': 'Alimentación tradicional (presencial)', 'imagen': 'presencial.jpg', 'servicio_tipo': 'tradicional', 'descripcion': 'Servicio de alimentación en restaurante y locales fijos'},
    {'nombre': 'Concesión de Casinos', 'imagen': 'casino.jpg', 'servicio_tipo': 'concesion', 'descripcion': 'Personal especializado para manejo de casinos empresariales'},
    {'nombre': 'Coffee break y eventos', 'imagen': 'cafeb.jpg', 'servicio_tipo': 'coffee', 'descripcion': 'Servicios de coffee break, eventos corporativos y sociales'},
    {'nombre': 'Repostería y snack con tickets', 'imagen': 'snack.jpg', 'servicio_tipo': 'reposteria', 'descripcion': 'Sistema de tickets para repostería y colaciones en empresas'},
]

for servicio_data in servicios_data:
    Servicio.objects.create(**servicio_data)

print('📂 Creando categorías...')
categorias_data = [
    {'nombre': 'Almuerzos', 'descripcion': 'Comidas principales del día, platos completos'},
    {'nombre': 'Bebidas', 'descripcion': 'Jugos naturales, bebidas calientes y refrescos'},
    {'nombre': 'Repostería', 'descripcion': 'Postres, dulces y productos de panadería'},
    {'nombre': 'Snacks', 'descripcion': 'Colaciones, aperitivos y comida rápida'},
    {'nombre': 'Vegetarianos', 'descripcion': 'Opciones sin carne, aptas para vegetarianos'},
    {'nombre': 'Veganos', 'descripcion': 'Opciones 100% vegetales, sin productos animales'},
    {'nombre': 'Desayunos', 'descripcion': 'Opciones para la primera comida del día'},
    {'nombre': 'Cenas', 'descripcion': 'Comidas ligeras para la noche'},
    {'nombre': 'Menús Ejecutivos', 'descripcion': 'Opciones completas para ejecutivos'},
    {'nombre': 'Servicios de Personal', 'descripcion': 'Personal especializado para eventos'},
]

for cat_data in categorias_data:
    Categoria.objects.create(**cat_data)

print('🍽️ Creando productos...')
# Solo crear algunos productos de ejemplo por espacio
servicio_transportado = Servicio.objects.get(servicio_tipo='transportado')
cat_almuerzos = Categoria.objects.get(nombre='Almuerzos')

productos_ejemplo = [
    {'nombre': 'Pollo a la chilena con arroz y ensalada', 'descripcion': 'Plato casero clásico, nutritivo y balanceado', 'precio': 4500, 'imagen': 'pollo a la chilena.png', 'categoria': cat_almuerzos, 'servicio': servicio_transportado},
    {'nombre': 'Lasagna de verduras gratinada', 'descripcion': 'Opción sin carne con variedad de vegetales frescos', 'precio': 4200, 'imagen': 'lasagna de verduras.png', 'categoria': cat_almuerzos, 'servicio': servicio_transportado},
]

for prod_data in productos_ejemplo:
    Producto.objects.create(**prod_data)

print('✅ Migración completa exitosa!')
print(f'📊 Servicios: {Servicio.objects.count()}')
print(f'📊 Categorías: {Categoria.objects.count()}')
print(f'📊 Productos: {Producto.objects.count()}')
"

echo ""
echo "🎉 ¡MIGRACIÓN COMPLETA!"
echo "========================"
echo "✅ Base de datos MySQL creada"
echo "✅ Tablas migradas"
echo "✅ Datos transferidos"
echo "✅ Superusuario creado (admin/admin123)"
echo ""
echo "🌐 Accede a:"
echo "• Django Admin: http://localhost:8000/admin/"
echo "• phpMyAdmin: http://localhost/phpmyadmin/"
echo "• Sitio web: http://localhost:8000/"
echo ""
echo "📝 Para ver la BD en phpMyAdmin:"
echo "• Servidor: localhost"
echo "• Usuario: root"
echo "• Contraseña: (vacía)"
echo "• Base de datos: gmexpress"