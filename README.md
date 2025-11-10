

<div align="center">
   <img src="static/images/gm express.png" alt="GM Express Logo" width="180"/>
   <h1>🚀 GM Express - Sistema de Gestión Completo</h1>
   <b>Sistema Django completo para la gestión de servicios de alimentación y eventos de <span style="color:#388e3c">GM Express</span>.</b>
   <br/>
   <i>Aplicación web funcional con CRUD completo, autenticación, validaciones de negocio y panel administrativo.</i>
</div>

---

## 📋 **DESCRIPCIÓN DEL PROYECTO**

GM-Express es una aplicación web desarrollada en Django 5.2.7 que proporciona un sistema integral de gestión para una empresa chilena de servicios de alimentación y catering. 

### **Características Principales:**
- ✅ **Sistema de Autenticación**: Login/Logout con protección de vistas
- ✅ **CRUD Completo**: Operaciones Create, Read, Update, Delete para todas las entidades
- ✅ **Validaciones de Negocio**: 
  - RUT chileno válido
  - Fechas en el pasado (no permitir fechas futuras)
  - Stock disponible antes de ventas
  - Duplicados de registros
  - Precios y cantidades positivas
- ✅ **Formularios con Validación**: Todos los formularios incluyen validaciones de formato y negocio
- ✅ **Panel Administrativo**: Dashboard con estadísticas y gestión completa
- ✅ **Sitio Web Responsive**: Catálogo público con Bootstrap 5
- ✅ **Base de Datos Poblada**: 50+ registros de prueba

---

## 🗂️ **ESTRUCTURA DEL PROYECTO**

```text
GM-Express/
│
├── 📁 APLICACIONES (4 Apps Django)
│   ├── usuarios/           # 👥 Gestión de usuarios y tipos
│   │   ├── models.py       # Usuario, TipoUsuario
│   │   ├── forms.py        # Formularios con validaciones
│   │   └── views.py        # CRUD completo
│   │
│   ├── catalogue/          # 📋 Catálogo de productos internos
│   │   ├── models.py       # Producto, Categoria (inventario)
│   │   ├── forms.py        # Validación stock, precios
│   │   └── views.py        # CRUD productos/categorías
│   │
│   ├── ventas/            # 💰 Sistema de ventas
│   │   ├── models.py       # Venta, DetalleVenta
│   │   ├── forms.py        # Validación fechas, montos, stock
│   │   └── views.py        # CRUD ventas y detalles
│   │
│   └── catalogo/          # 🌐 Catálogo web público
│       ├── models.py       # Servicio, Producto (web)
│       ├── forms.py        # Formularios servicios
│       └── views.py        # Vistas públicas + CRUD
│
├── 📁 CONFIGURACIÓN
│   ├── gmexpress/         # ⚙️ Configuración principal
│   │   ├── settings.py    # Base de datos, apps, zona horaria Chile
│   │   └── urls.py        # Todas las rutas (públicas y CRUD)
│   │
│   ├── templates/         # 🎨 Plantillas HTML
│   │   ├── templateEmpresa/    # Inicio, login, dashboard, info
│   │   ├── templateCatalogo/   # Catálogo público
│   │   ├── templateUsuarios/   # CRUD usuarios
│   │   ├── templateCatalogue/  # CRUD productos
│   │   └── templateVentas/     # CRUD ventas
│   │
│   └── static/           # 🖼️ CSS, imágenes y recursos
│
├── 📁 BASE DE DATOS
│   ├── db.sqlite3        # 🗄️ Base de datos SQLite (activa)
│   └── migrate_to_mysql.sh # 🔄 Script migración MySQL opcional
│
└── 📁 DOCUMENTACIÓN
    ├── README.md         # 📖 Este archivo
    ├── requirements.txt  # 📦 Dependencias del proyecto
    └── manage.py         # 🛠️ Script gestión Django
```

---

## 🚀 **INSTALACIÓN Y EJECUCIÓN**

### **📋 Requisitos Previos:**
- Python 3.11 o superior
- pip (gestor de paquetes de Python)
- Git (para clonar el repositorio)

### **⚙️ Pasos de Instalación:**

#### **1. Clonar el Repositorio:**
```bash
git clone https://github.com/PandaAkiraNakai/GM-Express.git
cd GM-Express
```

#### **2. Crear y Activar Entorno Virtual:**

**En Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**En Windows (CMD):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**En Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### **3. Instalar Dependencias:**
```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` contiene:
- Django==5.2.7
- pymysql==1.1.1
- asgiref==3.8.1
- sqlparse==0.5.2

#### **4. Aplicar Migraciones:**
```bash
python manage.py migrate
```

Este comando crea/actualiza todas las tablas en la base de datos SQLite.

#### **5. (Opcional) Poblar Base de Datos:**

La base de datos ya viene poblada con datos de prueba. Si necesitas repoblarla:

```bash
python poblar_servicios.py
```

#### **6. Iniciar el Servidor:**
```bash
python manage.py runserver
```

El servidor se iniciará en: **http://127.0.0.1:8000/**

---

## 🔐 **CREDENCIALES DE ACCESO**

### **Administrador Django (Admin Panel):**
- **URL**: http://127.0.0.1:8000/admin/
- **Usuario**: `admin`
- **Contraseña**: `admin123`

### **Acceso al Dashboard:**
- **URL**: http://127.0.0.1:8000/login/
- **Usuario**: `admin`
- **Contraseña**: `admin123`

---

## 🌐 **ESTRUCTURA DE URLS Y FUNCIONALIDADES**

### **📍 Rutas Públicas (sin autenticación):**
- **Inicio**: http://127.0.0.1:8000/
- **Catálogo**: http://127.0.0.1:8000/catalogo/
- **Productos**: http://127.0.0.1:8000/catalogo/catering-corporativo/
- **Nosotros**: http://127.0.0.1:8000/nosotros/
- **Login**: http://127.0.0.1:8000/login/

### **🔒 Rutas Protegidas (requieren login):**

#### **Dashboard:**
- http://127.0.0.1:8000/dashboard/

#### **CRUD Usuarios:**
- Lista: http://127.0.0.1:8000/usuarios/
- Crear: http://127.0.0.1:8000/usuarios/crear/
- Editar: http://127.0.0.1:8000/usuarios/{id}/editar/
- Eliminar: http://127.0.0.1:8000/usuarios/{id}/eliminar/
- Detalle: http://127.0.0.1:8000/usuarios/{id}/

#### **CRUD Tipos de Usuario:**
- Lista: http://127.0.0.1:8000/tipos-usuario/
- Crear: http://127.0.0.1:8000/tipos-usuario/crear/
- Editar: http://127.0.0.1:8000/tipos-usuario/{id}/editar/
- Eliminar: http://127.0.0.1:8000/tipos-usuario/{id}/eliminar/

#### **CRUD Categorías:**
- Lista: http://127.0.0.1:8000/categorias/
- Crear: http://127.0.0.1:8000/categorias/crear/
- Editar: http://127.0.0.1:8000/categorias/{id}/editar/
- Eliminar: http://127.0.0.1:8000/categorias/{id}/eliminar/

#### **CRUD Productos:**
- Lista: http://127.0.0.1:8000/productos/
- Crear: http://127.0.0.1:8000/productos/crear/
- Editar: http://127.0.0.1:8000/productos/{id}/editar/
- Eliminar: http://127.0.0.1:8000/productos/{id}/eliminar/
- Detalle: http://127.0.0.1:8000/productos/{id}/

#### **CRUD Ventas:**
- Lista: http://127.0.0.1:8000/ventas/
- Crear: http://127.0.0.1:8000/ventas/crear/
- Editar: http://127.0.0.1:8000/ventas/{id}/editar/
- Eliminar: http://127.0.0.1:8000/ventas/{id}/eliminar/
- Detalle: http://127.0.0.1:8000/ventas/{id}/
- Agregar Producto: http://127.0.0.1:8000/ventas/{id}/agregar-producto/

#### **CRUD Servicios:**
- Lista: http://127.0.0.1:8000/servicios/
- Crear: http://127.0.0.1:8000/servicios/crear/
- Editar: http://127.0.0.1:8000/servicios/{id}/editar/
- Eliminar: http://127.0.0.1:8000/servicios/{id}/eliminar/

---

## ✅ **VALIDACIONES IMPLEMENTADAS**

### **Validaciones de Formato:**
- ✅ RUT chileno con dígito verificador válido
- ✅ Correos electrónicos únicos
- ✅ Teléfonos en formato chileno
- ✅ Contraseñas seguras (9+ caracteres, mayúscula, símbolo)
- ✅ Slug de servicios en minúsculas con guiones

### **Validaciones de Negocio:**
- ✅ **Fechas en el pasado**: No permitir ventas o nacimientos futuros
- ✅ **Stock disponible**: Verificar antes de vender
- ✅ **Duplicados**: Evitar nombres/RUTs/correos duplicados
- ✅ **Valores positivos**: Precios, cantidades, montos > 0
- ✅ **Edad mínima**: Usuarios deben tener 18+ años
- ✅ **Relaciones protegidas**: No eliminar si hay registros dependientes

---

## 📊 **DATOS DE PRUEBA**

La base de datos incluye:
- **10+ Usuarios** con datos chilenos reales
- **3 Tipos de Usuario**: Administrador, Cliente, Empleado
- **4 Categorías**: Almuerzos, Bebidas, Repostería, Snacks
- **31 Productos** con precios y stock
- **6 Servicios**: Catering, Eventos, Delivery, etc.
- **Múltiples Ventas** con detalles

---

## 🛠️ **COMANDOS ÚTILES**

### **Gestión de Base de Datos:**
```bash
# Crear migraciones después de cambios en models.py
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario (si necesitas otro)
python manage.py createsuperuser
```

### **Comandos Personalizados:**
```bash
# Verificar servicios activos
python manage.py crear_servicios

# Actualizar imágenes de productos
python manage.py actualizar_imagenes
```

### **Servidor de Desarrollo:**
```bash
# Iniciar servidor
python manage.py runserver

# Iniciar en otro puerto
python manage.py runserver 8080

# Iniciar accesible desde red local
python manage.py runserver 0.0.0.0:8000
```

---

## 🔧 **CONFIGURACIÓN DE BASE DE DATOS**

### **SQLite (Actual - Desarrollo):**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### **MySQL (Opcional - Comentado en settings.py):**
Requiere XAMPP con MariaDB 10.5+
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gmexpress',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

## 📱 **TECNOLOGÍAS UTILIZADAS**

- **Backend**: Django 5.2.7 (Python)
- **Base de Datos**: SQLite (desarrollo), MySQL compatible
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Autenticación**: Django Auth
- **Localización**: Español chileno (es-cl)
- **Zona Horaria**: America/Santiago

---

## 📝 **NOTAS IMPORTANTES**

### **Para Desarrollo:**
- `DEBUG = True` - Solo para desarrollo
- `SECRET_KEY` es insegura - cambiar en producción
- Imágenes se referencian como rutas de texto en `static/images/`

### **Para Producción:**
- Cambiar `DEBUG = False`
- Generar nueva `SECRET_KEY` segura
- Configurar `ALLOWED_HOSTS`
- Usar base de datos MySQL/PostgreSQL
- Ejecutar `python manage.py collectstatic`
- Configurar servidor web (Nginx/Apache) con Gunicorn

### **Para Despliegue en AWS:**
1. Instalar dependencias: `pip install -r requirements.txt`
2. Configurar variables de entorno para credenciales DB
3. Aplicar migraciones: `python manage.py migrate`
4. Recopilar archivos estáticos: `python manage.py collectstatic`
5. Configurar Nginx/Apache como proxy inverso
6. Usar Gunicorn como servidor WSGI

---

## 🎯 **CUMPLIMIENTO DE REQUISITOS**

### **✅ Requisitos Funcionales:**
- [x] Implementación de todos los formularios (excepto transaccionales)
- [x] Validaciones de formato (RUT, email, teléfono, etc.)
- [x] Validaciones de negocio (fechas pasadas, duplicados, stock)
- [x] Sistema de autenticación (login/logout)
- [x] Acceso protegido a vistas sensibles (@login_required)
- [x] CRUD completo para todas las entidades

### **✅ Requisitos Técnicos:**
- [x] Configuración de base de datos en settings.py
- [x] Archivo requirements.txt incluido
- [x] README.md con instrucciones completas
- [x] Credenciales de prueba documentadas
- [x] Proyecto ejecutable con `python manage.py runserver`
- [x] Código limpio, documentado y estructurado

---

## 👨‍💻 **AUTOR**

**Proyecto**: GM-Express
**Repositorio**: https://github.com/PandaAkiraNakai/GM-Express
**Curso**: Programación Back End
**Institución**: INACAP
**Fecha**: Noviembre 2025

---

## 📞 **CONTACTO GM-EXPRESS**

- **Teléfono**: +569 7615 9518 / +569 4785 4598
- **Email**: ventas@gmexpress.cl / proveedores@gmexpress.cl
- **Facebook**: https://www.facebook.com/GMEXPRESSCL
- **Instagram**: https://www.instagram.com/gmexpress_cl/

---

<div align="center">
   <b>✨ Proyecto completamente funcional y listo para despliegue ✨</b>
</div>

### **� Características Principales:**
- ✅ **4 Aplicaciones Django** independientes
- ✅ **Sistema de autenticación** completo
- ✅ **Panel administrativo** personalizado
- ✅ **Sitio web responsive** con Bootstrap 5
- ✅ **Base de datos** poblada con datos reales
- ✅ **50+ registros** de servicios, productos y usuarios
- ✅ **32 imágenes** asignadas automáticamente

---

## 🗂️ **Estructura del Proyecto**

```text
GM-Express/
│
├── 📁 APLICACIONES PRINCIPALES
│   ├── usuarios/           # 👥 Gestión de usuarios y tipos
│   ├── catalogue/          # 📋 Catálogo de productos y categorías  
│   ├── ventas/            # 💰 Sistema de ventas y detalles
│   └── catalogo/          # 🌐 Navegación web y servicios
│
├── 📁 CONFIGURACIÓN
│   ├── gmexpress/         # ⚙️ Configuración principal Django
│   ├── templates/         # 🎨 Plantillas HTML responsive
│   └── static/           # 🖼️ CSS, imágenes y recursos
│
├── 📁 BASE DE DATOS
│   ├── db.sqlite3        # 🗄️ Base de datos SQLite
│   └── migrate_to_mysql.sh # 🔄 Script migración MySQL
│
└── 📁 DOCUMENTACIÓN
    ├── README.md         # 📖 Este archivo
    ├── CHECKLIST.md      # ✅ Lista verificación completa
    └── manage.py         # 🛠️ Script gestión Django
```

---

## � **Aplicaciones del Sistema**

### **👥 `usuarios` - Gestión de Usuarios**
| Modelo | Descripción | Registros |
|--------|-------------|-----------|
| `TipoUsuario` | Tipos: Cliente, Admin, Empleado | 3 tipos |
| `Usuario` | Usuarios con datos chilenos reales | 10+ usuarios |

### **📋 `catalogue` - Catálogo de Productos**
| Modelo | Descripción | Registros |
|--------|-------------|-----------|
| `Categoria` | Almuerzos, Bebidas, Repostería, Snacks | 4 categorías |
| `Producto` | Productos alimenticios con precios | 31 productos |

### **💰 `ventas` - Sistema de Ventas**
| Modelo | Descripción | Registros |
|--------|-------------|-----------|
| `Venta` | Transacciones con usuarios | Múltiples ventas |
| `DetalleVenta` | Detalles de productos vendidos | Detalles completos |

### **🌐 `catalogo` - Navegación Web**
| Modelo | Descripción | Registros |
|--------|-------------|-----------|
| `Servicio` | Servicios de GM-Express | 6 servicios |
| `Producto` | Productos para navegación web | 31 productos |

---

## 🌐 **Sitio Web y Navegación**

### **🏠 Páginas Principales:**
- **🏠 Inicio:** `http://127.0.0.1:8000/` - Servicios con imágenes
- **📋 Catálogo:** `http://127.0.0.1:8000/catalogo/tradicional/` - Productos
- **📊 Dashboard:** `http://127.0.0.1:8000/dashboard/` - Panel administrativo
- **⚙️ Admin:** `http://127.0.0.1:8000/admin/` - Administración Django

### **🎨 Características del Sitio:**
- ✅ **Responsive Design** con Bootstrap 5
- ✅ **Navegación intuitiva** entre servicios
- ✅ **Imágenes automáticas** para productos
- ✅ **Autenticación** de usuarios
- ✅ **Dashboard administrativo** con estadísticas

---

## 🔐 **Acceso y Credenciales**

### **👨‍💼 Usuario Administrador:**
```
Usuario: admin
Contraseña: admin123

---

## 🛠️ **Instalación y Ejecución**

### **📋 Requisitos:**
- Python 3.11+
- Django 5.2.7
- SQLite (incluido)

### **🚀 Instalación Rápida:**

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/PandaAkiraNakai/GM-Express.git
   cd GM-Express
   ```

2. **Crea y activa entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # venv\Scripts\activate   # Windows
   ```

3. **Instala dependencias:**
   ```bash
   pip install django
   ```

4. **Ejecuta migraciones:**
   ```bash
   python manage.py migrate
   ```

5. **Inicia el servidor:**
   ```bash
   python manage.py runserver
   ```

6. **Accede al sitio:**
   - Abre: `http://127.0.0.1:8000/`

---

## �️ **Comandos Personalizados**

### **📊 Verificar Servicios:**
```bash
python manage.py crear_servicios
```

### **🖼️ Actualizar Imágenes:**
```bash
python manage.py actualizar_imagenes
```

### **🔄 Migrar a MySQL:**
```bash
./migrate_to_mysql.sh
```

---

## 🔄 **Base de Datos**

### **🗄️ SQLite (Desarrollo):**
- ✅ **Configurado** y funcionando
- ✅ **Datos migrados** completamente
- ✅ **Listo para desarrollo**

### **� MySQL (Producción):**
- ✅ **Script de migración** creado
- ✅ **Configuración XAMPP** disponible
- ✅ **Comandos automáticos** incluidos

---

## 📝 **Documentación Adicional**

- **📋 [CHECKLIST.md](CHECKLIST.md)** - Lista completa de verificación
- **🔧 [catalogo/management/commands/](catalogo/management/commands/)** - Comandos personalizados
- **🎨 [static/CSS/style.css](static/CSS/style.css)** - Estilos personalizados
- **📊 [templates/](templates/)** - Plantillas HTML

---

## 🤝 **Contribuciones**

Sergio el Nazer
Savkapleito
Dante's Inferno

---

<div align="center">
   <b>🎉 ¡Proyecto GM-Express completado exitosamente! 🎉</b>
   <br/>
   <i>Desarrollado con Django 5.2.7 • Bootstrap 5 • SQLite/MySQL</i>
</div>
   <img src="static/images/servicio.png" alt="Servicio GM Express" width="120"/>
</div>
