

<div align="center">
   <img src="static/images/gm express.png" alt="GM Express Logo" width="180"/>
   <h1>Backend GM Express</h1>
   <b>Backend desarrollado en Django para la gestión de servicios de alimentación y eventos de <span style="color:#388e3c">GM Express</span>.</b>
   <br/>
   <i>Organiza información institucional, catálogo de productos y servicios, y presentación web moderna.</i>
</div>

---


## 🗂️ Estructura del Proyecto

```text
GM-Express/
│
├── db.sqlite3             # Base de datos SQLite
├── manage.py              # Script de gestión Django
├── README.md              # Este archivo
│
├── catalogo/              # Lógica y datos del catálogo
│   ├── models.py          # Modelos de productos y servicios
│   ├── views.py           # Vistas del catálogo
│   └── ...
│
├── empresa/               # Información institucional
│   ├── models.py          # Modelos de empresa
│   ├── views.py           # Vistas de empresa
│   └── ...
│
├── gmexpress/             # Configuración principal Django
│   ├── settings.py        # Ajustes del proyecto
│   ├── urls.py            # Rutas principales
│   └── ...
│
├── static/                # Archivos estáticos (CSS, imágenes)
│   ├── CSS/
│   │   └── style.css
│   └── images/
│
└── templates/             # Plantillas HTML
   ├── templateCatalogo/
   │   ├── catalogo2.html
   │   └── catalogo3.html
   └── templateEmpresa/
      ├── inicio.html
      └── info.html
```
│   │   └── style.css
│   └── images/
│
└── templates/
    ├── templateCatalogo/
    │   ├── catalogo2.html
    │   └── catalogo3.html
    └── templateEmpresa/
        ├── inicio.html
        └── info.html
```


## 📝 Descripción General

| Carpeta/Archivo   | Descripción |
|-------------------|-------------|
| `catalogo/`       | Lógica y datos del catálogo de productos y servicios (menús, snacks, transporte, etc.). Ver [`catalogo/models.py`](catalogo/models.py) |
| `empresa/`        | Información institucional: historia, misión, visión, valores, contactos y redes sociales. Ver [`empresa/views.py`](empresa/views.py) |
| `gmexpress/`      | Configuración principal del proyecto Django (ajustes, rutas, etc.) |
| `static/`         | Archivos estáticos: CSS y recursos de imágenes. Paleta de verdes personalizada en [`static/CSS/style.css`](static/CSS/style.css) |
| `templates/`      | Plantillas HTML para la presentación web, organizadas por área |


## 🚀 Funcionalidades

- Visualización de información institucional: historia, misión, visión, valores, contactos y redes sociales.
- Catálogo de productos y servicios con imágenes, descripciones, ingredientes/componentes, tiempos de entrega y condiciones de consumo.
- Navegación intuitiva entre diferentes tipos de menús y servicios.
- Interfaz moderna y responsiva basada en **Bootstrap** y estilos personalizados.


## 🛠️ Instalación y Ejecución

1. **Clona el repositorio:**
   ```sh
   git clone <url-del-repositorio>
   cd GM-Express
   ```
2. **Instala las dependencias necesarias (Django):**
   ```sh
   pip install django
   ```
3. **Ejecuta las migraciones:**
   ```sh
   python manage.py migrate
   ```
4. **Inicia el servidor de desarrollo:**
   ```sh
   python manage.py runserver
   ```
5. Accede a la aplicación en [http://localhost:8000/](http://localhost:8000/)


---

## 👥 Créditos

- Bizcochitos y su Proyecto

<div align="center">
   <img src="static/images/servicio.png" alt="Servicio GM Express" width="120"/>
</div>
