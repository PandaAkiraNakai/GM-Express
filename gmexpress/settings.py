from pathlib import Path
import os
import pymysql

# Instalar pymysql como MySQLdb
pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#Variable Ruta Templates
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-26mixdtc!h2+&1#c0or@c7=q79p4v)l)0qg12+93g7^7k+-mk9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'empresa',
    'catalogo',
    'usuarios',
    'ventas',
    'catalogue',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gmexpress.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gmexpress.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# Configuración SQLite (recomendada para desarrollo)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuración MySQL para XAMPP (comentada - requiere MariaDB 10.5+)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'gmexpress',
#         'USER': 'root',  # Usuario por defecto de XAMPP
#         'PASSWORD': '',  # Contraseña vacía por defecto en XAMPP
#         'HOST': 'localhost',
#         'PORT': '3306',  # Puerto por defecto de MySQL en XAMPP
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         },
#     }
# }

# Configuración SQLite original (comentada para desarrollo)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
# Directorio de archivos estáticos para desarrollo (donde buscará archivos estáticos adicionales)
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Directorio de archivos estáticos para producción (donde collectstatic los recopila)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files (User uploaded content)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Nota: STATIC_DIRS no es una configuración válida de Django y se elimina para evitar confusión.
# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# URLs de redirección para autenticación
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'

# ========== CONFIGURACIÓN PARA PRODUCCIÓN AWS ==========
# Detecta si está corriendo en AWS Elastic Beanstalk
if 'RDS_HOSTNAME' in os.environ:
    # Modo producción en AWS
    DEBUG = False
    ALLOWED_HOSTS = ['.elasticbeanstalk.com', '.amazonaws.com', '*']
    
    # Opcional: Configuración para usar RDS MySQL en AWS
    # Descomenta si configuras una base de datos RDS
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.mysql',
    #         'NAME': os.environ.get('RDS_DB_NAME', 'gmexpress'),
    #         'USER': os.environ.get('RDS_USERNAME', 'admin'),
    #         'PASSWORD': os.environ.get('RDS_PASSWORD', ''),
    #         'HOST': os.environ.get('RDS_HOSTNAME', 'localhost'),
    #         'PORT': os.environ.get('RDS_PORT', '3306'),
    #     }
    # }
else:
    # Modo desarrollo local (mantiene configuración actual)
    pass
