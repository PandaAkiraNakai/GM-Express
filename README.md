

<div align="center">
   <img src="static/images/gm express.png" alt="GM Express Logo" width="180"/>
   <h1>🚀 GM Express - Sistema Completo</h1>
   <b>Sistema Django completo para la gestión de servicios de alimentación y eventos de <span style="color:#388e3c">GM Express</span>.</b>
   <br/>
   <i>Proyecto 100% funcional con 4 aplicaciones Django, sistema de autenticación, panel administrativo y sitio web responsive.</i>
</div>

---

## 🎯 **ESTADO DEL PROYECTO:

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
