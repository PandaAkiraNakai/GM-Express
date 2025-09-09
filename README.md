# GMExpress

Este proyecto corresponde al backend de GM Express, una empresa chilena de servicios de alimentación y eventos. El sistema está desarrollado en Django y organiza la información de la empresa, su catálogo de productos y servicios, y la gestión de vistas y plantillas para la presentación web.

## Estructura del Proyecto

```
Backend1/
│
├── db.sqlite3
├── manage.py
├── README.md
│
├── catalogo/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── __pycache__/
│   └── migrations/
│
├── empresa/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── __pycache__/
│   └── migrations/
│
├── gmexpress/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/
│
├── static/
│   ├── CSS/
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

## Descripción General

- **catalogo/**: Contiene la lógica y los datos del catálogo de productos y servicios, incluyendo menús para transporte, eventos, snacks, presencial, y servicios adicionales. Los datos están definidos en diccionarios dentro de [`catalogo.models`](catalogo/models.py).
- **empresa/**: Incluye la información institucional de la empresa (historia, misión, visión, valores, contactos y redes sociales) y las vistas asociadas. Ver [`empresa.views`](empresa/views.py).
- **gmexpress/**: Configuración principal del proyecto Django (ajustes, rutas, etc.).
- **static/**: Archivos estáticos como hojas de estilo CSS y recursos de imágenes. El diseño utiliza una paleta de verdes personalizada en [`static/CSS/style.css`](static/CSS/style.css).
- **templates/**: Plantillas HTML para la presentación web, organizadas en carpetas para el catálogo y la empresa.

## Funcionalidades

- Visualización de la información de la empresa: historia, misión, visión, valores, contactos y redes sociales.
- Catálogo de productos y servicios con imágenes, descripciones, ingredientes/componentes, tiempos de entrega y condiciones de consumo.
- Navegación entre diferentes tipos de menús y servicios.
- Interfaz moderna y responsiva basada en Bootstrap y estilos personalizados.

## Ejecución del Proyecto

1. Instala las dependencias necesarias (Django).
2. Ejecuta las migraciones si es necesario:
   ```sh
   python manage.py migrate
   ```
3. Inicia el servidor de desarrollo:
   ```sh
   python manage.py runserver
   ```
4. Accede a la aplicación en `http://localhost:8000/`.

## Créditos

- Bizcochitos y su Proyecto
