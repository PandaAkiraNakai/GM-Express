from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from empresa import views as vista
from catalogo import views as catalogo_vista
from usuarios import views as usuarios_vista
from catalogue import views as catalogue_vista
from ventas import views as ventas_vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vista.inicio, name='inicio'),
    
    # ==================== RUTAS DE AUTENTICACIÓN ====================
    path('login/', vista.login_view, name='login'),
    path('logout/', vista.logout_view, name='logout'),
    path('dashboard/', vista.dashboard, name='dashboard'),
    
    # ==================== RUTAS CATÁLOGO PÚBLICO ====================
    path('catalogo/', catalogo_vista.catalogoServicios, name='catalogo'),
    path('catalogo/<str:servicio_tipo>/', catalogo_vista.catalogoProductos, name='catalogo_productos'),
    path('catalogo/<str:servicio_tipo>/<int:producto_id>/', catalogo_vista.catalogoMenu, name='menu_detalle'),
    
    # ==================== RUTAS INFORMACIÓN EMPRESA ====================
    path('nosotros/', vista.info_empresa, name='info_empresa'),
    
    # ==================== CRUD USUARIOS ====================
    # Tipo de Usuario
    path('tipos-usuario/', usuarios_vista.tipo_usuario_lista, name='tipo_usuario_lista'),
    path('tipos-usuario/crear/', usuarios_vista.tipo_usuario_crear, name='tipo_usuario_crear'),
    path('tipos-usuario/<int:pk>/editar/', usuarios_vista.tipo_usuario_editar, name='tipo_usuario_editar'),
    path('tipos-usuario/<int:pk>/eliminar/', usuarios_vista.tipo_usuario_eliminar, name='tipo_usuario_eliminar'),
    
    # Usuario
    path('usuarios/', usuarios_vista.usuario_lista, name='usuario_lista'),
    path('usuarios/<int:pk>/', usuarios_vista.usuario_detalle, name='usuario_detalle'),
    path('usuarios/crear/', usuarios_vista.usuario_crear, name='usuario_crear'),
    path('usuarios/<int:pk>/editar/', usuarios_vista.usuario_editar, name='usuario_editar'),
    path('usuarios/<int:pk>/eliminar/', usuarios_vista.usuario_eliminar, name='usuario_eliminar'),
    
    # ==================== CRUD CATALOGUE (Productos Internos) ====================
    # Categoría
    path('categorias/', catalogue_vista.categoria_lista, name='categoria_lista'),
    path('categorias/crear/', catalogue_vista.categoria_crear, name='categoria_crear'),
    path('categorias/<int:pk>/editar/', catalogue_vista.categoria_editar, name='categoria_editar'),
    path('categorias/<int:pk>/eliminar/', catalogue_vista.categoria_eliminar, name='categoria_eliminar'),
    
    # Producto
    path('productos/', catalogue_vista.producto_lista, name='producto_lista'),
    path('productos/<int:pk>/', catalogue_vista.producto_detalle, name='producto_detalle'),
    path('productos/crear/', catalogue_vista.producto_crear, name='producto_crear'),
    path('productos/<int:pk>/editar/', catalogue_vista.producto_editar, name='producto_editar'),
    path('productos/<int:pk>/eliminar/', catalogue_vista.producto_eliminar, name='producto_eliminar'),
    
    # ==================== CRUD VENTAS ====================
    # Venta
    path('ventas/', ventas_vista.venta_lista, name='venta_lista'),
    path('ventas/<int:pk>/', ventas_vista.venta_detalle, name='venta_detalle'),
    path('ventas/crear/', ventas_vista.venta_crear, name='venta_crear'),
    path('ventas/<int:pk>/editar/', ventas_vista.venta_editar, name='venta_editar'),
    path('ventas/<int:pk>/eliminar/', ventas_vista.venta_eliminar, name='venta_eliminar'),
    
    # Detalle Venta
    path('ventas/<int:venta_id>/agregar-producto/', ventas_vista.detalle_crear, name='detalle_crear'),
    path('detalles/<int:pk>/eliminar/', ventas_vista.detalle_eliminar, name='detalle_eliminar'),
    
    # ==================== CRUD SERVICIOS WEB ====================
    path('servicios/', catalogo_vista.servicio_lista, name='servicio_lista'),
    path('servicios/crear/', catalogo_vista.servicio_crear, name='servicio_crear'),
    path('servicios/<int:pk>/editar/', catalogo_vista.servicio_editar, name='servicio_editar'),
    path('servicios/<int:pk>/eliminar/', catalogo_vista.servicio_eliminar, name='servicio_eliminar'),
]

# Servir archivos media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
