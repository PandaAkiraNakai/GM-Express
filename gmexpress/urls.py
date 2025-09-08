from django.contrib import admin
from django.urls import path

from empresa import views as vista
from catalogo import views as catalogo_vista
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vista.inicio, name='inicio'),
    
    #path catalogos    
    path('catalogo/', catalogo_vista.catalogoServicios, name='catalogo'),
    path('catalogo/<str:servicio_tipo>/', catalogo_vista.catalogoProductos, name='catalogo_productos'),
    
    #path menu detalles
    path('catalogo/<str:servicio_tipo>/<int:producto_id>/', catalogo_vista.catalogoMenu, name='menu_detalle'),
    
    #path nosotros
    path('nosotros/', vista.info_empresa, name='info_empresa'),
]
