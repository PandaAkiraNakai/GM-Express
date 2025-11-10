# GM-Express: Copilot Instructions

## Project Overview
Django 5.2.7 application for GM-Express, a Chilean food service and catering company. The system manages services, products, users, and sales with a public-facing catalog and authenticated admin dashboard.

## Architecture

### Multi-App Structure (5 Django Apps)
- **`empresa`**: Core views (landing, login, dashboard, company info) - acts as the main controller
- **`catalogo`**: Public-facing catalog with `Servicio` and `Producto` models for web navigation
- **`catalogue`**: Internal product management with `Categoria` and `Producto` models for business operations
- **`usuarios`**: User management with `Usuario` and `TipoUsuario` models
- **`ventas`**: Sales system with `Venta` and `DetalleVenta` models

**Critical**: `catalogo` and `catalogue` are separate apps with different purposes - `catalogo` is for web display, `catalogue` is for inventory/sales operations. Do not confuse them.

### Database Tables
All models explicitly define `db_table` in Meta classes. Never rely on Django's auto-generated table names:
- `servicio`, `producto_catalogo`, `categoria_catalogo` (catalogo app)
- `producto`, `categoria` (catalogue app)
- `usuario`, `tipo_usuario` (usuarios app)
- `ventas`, `detalle_ventas` (ventas app)

## Key Conventions

### Choices Pattern
Status/enum fields use imported choices from `<app>/choices.py`:
```python
from usuarios.choices import estado
# Then in model:
estado = models.CharField(max_length=1, choices=estado, default='1')
```
- `estado`: '1' = Activo/Pendiente, '0' = Inactivo (used in usuarios, catalogue, catalogo)
- `ventas.estado`: '1'-'5' for Pendiente/En Proceso/Completado/Cancelado/Devuelto
- `tipo_venta`: 'p' = Producto

### Foreign Key Pattern
Always use `on_delete=models.PROTECT` and `limit_choices_to={'estado': '1'}` for active records:
```python
categoria_id = models.ForeignKey(Categoria, on_delete=models.PROTECT, 
                                 limit_choices_to={'estado': '1'})
```

### URL Routing
- Main routes in `gmexpress/urls.py` - no app-specific `urls.py` files exist
- Service catalog URLs use `servicio_tipo` slug: `/catalogo/<servicio_tipo>/`
- Product detail URLs: `/catalogo/<servicio_tipo>/<producto_id>/`

### Chilean Localization
- `settings.py`: `LANGUAGE_CODE = 'es-cl'`, `TIME_ZONE = 'America/Santiago'`
- Chilean RUT validation in `Usuario.run` field
- All user-facing text in Spanish

## Development Workflow

### Database Management
- **Active DB**: SQLite (`db.sqlite3`) - default for development
- **MySQL Support**: Commented config in `settings.py` - requires MariaDB 10.5+, XAMPP setup
- Uses `pymysql` as MySQLdb adapter (installed at settings top)

### Custom Management Commands
Located in `catalogo/management/commands/`:
- `python manage.py crear_servicios` - Verify/activate services
- `python manage.py actualizar_imagenes` - Update product images

### Data Population
- `poblar_servicios.py` - Standalone script to seed initial services (run directly, not via manage.py)
- Pre-populated with 50+ records across all models

### Static Files
- `STATIC_URL = 'static/'`
- `STATICFILES_DIRS = [BASE_DIR / 'static']` - development source
- `STATIC_ROOT = BASE_DIR / 'staticfiles'` - production collectstatic target
- Images stored as CharField paths (e.g., `'default.jpg'`, `'catering.jpg'`)

### Authentication
- Uses Django's built-in `authenticate`, `login`, `logout` from `django.contrib.auth`
- `@login_required` decorator on dashboard and logout views
- Login view in `empresa/views.py` redirects to `dashboard` on success
- Credentials: admin/admin123

## Common Patterns

### View Structure (empresa/views.py)
All main views in `empresa` app import models from other apps:
```python
from catalogo.models import Servicio
from catalogue.models import Categoria, Producto
from usuarios.models import Usuario
from ventas.models import Venta, DetalleVenta
```

### Template Organization
- `templates/templateEmpresa/`: inicio, login, dashboard, info
- `templates/templateCatalogo/`: catalogo2 (products), catalogo3 (detail)
- Bootstrap 5 responsive design

### Dashboard Logic
Aggregates cross-app statistics using `.count()` and `.order_by('-fecha_venta')[:5]`

## Critical Files
- `gmexpress/settings.py` - Database config, installed apps, Chilean locale
- `gmexpress/urls.py` - All URL routing (no app-level urls)
- `empresa/views.py` - Main controller logic
- `catalogo/views.py` - Public catalog display logic
- `**/choices.py` - Enum definitions

## Testing & Running
```bash
python manage.py runserver  # Default: http://127.0.0.1:8000/
python manage.py migrate    # Apply migrations
```

## Notes
- Secret key is development-only (marked INSECURE)
- `DEBUG = True` - not production-ready
- No REST API endpoints - traditional Django template rendering
- No app named 'empresa' in models - it only contains views
