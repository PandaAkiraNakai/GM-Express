# 🚀 GUÍA DE DESPLIEGUE EN AWS - GM EXPRESS

## 📋 Requisitos Previos

- Cuenta de AWS activa
- Proyecto GM-Express completo
- Git instalado
- Conocimientos básicos de terminal/bash

---

## 🎯 OPCIONES DE DESPLIEGUE EN AWS

### **OPCIÓN 1: AWS Elastic Beanstalk (Recomendada - Más Fácil)**

#### Ventajas:
- ✅ Configuración automática
- ✅ Escalado automático
- ✅ Ideal para Django
- ✅ Administración simplificada

#### Pasos:

1. **Preparar el Proyecto**

```bash
# En la carpeta del proyecto
pip install awsebcli

# Inicializar Elastic Beanstalk
eb init -p python-3.11 gm-express --region us-east-1

# Cuando pregunte por CodeCommit, responde: No
```

2. **Crear archivo .ebextensions/django.config**

```bash
mkdir .ebextensions
```

Crear archivo `.ebextensions/django.config`:

```yaml
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: gmexpress.wsgi:application
  aws:elasticbeanstalk:application:environment:
    DJANGO_SETTINGS_MODULE: gmexpress.settings
```

3. **Crear archivo .ebignore**

```
venv/
*.pyc
__pycache__/
.git/
*.sqlite3
```

4. **Configurar settings.py para producción**

Agregar al final de `gmexpress/settings.py`:

```python
# AWS Elastic Beanstalk Configuration
if 'RDS_HOSTNAME' in os.environ:
    DEBUG = False
    ALLOWED_HOSTS = ['.elasticbeanstalk.com', '.amazonaws.com', '*']
    
    # Opcional: Cambiar a RDS MySQL
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
```

5. **Desplegar**

```bash
# Crear entorno y desplegar
eb create gm-express-env

# Esperar 5-10 minutos...

# Ver la URL del sitio
eb open
```

6. **Aplicar Migraciones**

```bash
# SSH al servidor
eb ssh

# Navegar al directorio
cd /var/app/current

# Activar entorno virtual
source /var/app/venv/*/bin/activate

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Salir
exit
```

---

### **OPCIÓN 2: AWS EC2 con Ubuntu (Más Control)**

#### Pasos:

1. **Crear Instancia EC2**

- Ingresar a AWS Console → EC2
- Lanzar Instancia
- Seleccionar: Ubuntu Server 22.04 LTS
- Tipo: t2.micro (elegible para capa gratuita)
- Configurar grupo de seguridad:
  - SSH (puerto 22) - Tu IP
  - HTTP (puerto 80) - Anywhere
  - Custom TCP (puerto 8000) - Anywhere
- Crear/Descargar par de claves .pem

2. **Conectar a la Instancia**

```bash
# Windows PowerShell
ssh -i "tu-clave.pem" ubuntu@tu-ip-publica-ec2

# Una vez conectado:
sudo apt update
sudo apt upgrade -y
```

3. **Instalar Dependencias**

```bash
# Python y pip
sudo apt install python3-pip python3-venv git -y

# Clonar repositorio
git clone https://github.com/PandaAkiraNakai/GM-Express.git
cd GM-Express

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
pip install gunicorn
```

4. **Configurar Django para Producción**

Editar `gmexpress/settings.py`:

```python
DEBUG = False
ALLOWED_HOSTS = ['tu-ip-publica-ec2', 'tu-dominio.com', '*']
```

5. **Aplicar Migraciones**

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

6. **Configurar Gunicorn**

Crear `/etc/systemd/system/gunicorn.service`:

```ini
[Unit]
Description=Gunicorn daemon for GM Express
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/GM-Express
ExecStart=/home/ubuntu/GM-Express/venv/bin/gunicorn \
    --workers 3 \
    --bind 0.0.0.0:8000 \
    gmexpress.wsgi:application

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

7. **Acceder al Sitio**

```
http://tu-ip-publica-ec2:8000/
```

---

### **OPCIÓN 3: AWS Lightsail (Más Simple y Económica)**

#### Pasos:

1. **Crear Instancia Lightsail**

- Ingresar a AWS Console → Lightsail
- Crear Instancia
- Seleccionar: Linux/Unix - Ubuntu 22.04
- Plan: $3.50/mes (o prueba gratuita)
- Nombre: gm-express
- Crear Instancia

2. **Configurar Firewall**

- En la instancia, ir a "Networking"
- Agregar regla: Custom TCP 8000, Anywhere

3. **Conectar vía SSH**

- Clic en "Connect using SSH" (desde el navegador)
- O usar SSH key descargada

4. **Seguir Pasos de EC2** (puntos 3-7 de la Opción 2)

---

## 📦 ARCHIVO requirements.txt ACTUALIZADO PARA AWS

Crear/actualizar `requirements.txt`:

```
Django==5.2.7
pymysql==1.1.1
asgiref==3.8.1
sqlparse==0.5.2
gunicorn==21.2.0
```

---

## 🔧 CONFIGURACIÓN ADICIONAL

### **Archivo .gitignore**

```
venv/
*.pyc
__pycache__/
.env
db.sqlite3
*.log
staticfiles/
```

### **Archivo .env para variables de entorno**

```env
SECRET_KEY=tu-secret-key-segura
DEBUG=False
ALLOWED_HOSTS=tu-dominio.com,tu-ip-ec2
```

---

## ✅ CHECKLIST ANTES DE DESPLEGAR

- [ ] `requirements.txt` actualizado
- [ ] `DEBUG = False` en producción
- [ ] `ALLOWED_HOSTS` configurado
- [ ] Migraciones aplicadas
- [ ] Superusuario creado
- [ ] `collectstatic` ejecutado
- [ ] Base de datos poblada
- [ ] Credenciales documentadas

---

## 🌐 VERIFICACIÓN POST-DESPLIEGUE

1. **Acceder a la URL pública**
```
http://tu-dominio-aws/
```

2. **Probar Login**
```
http://tu-dominio-aws/login/
Usuario: admin
Contraseña: admin123
```

3. **Probar Dashboard**
```
http://tu-dominio-aws/dashboard/
```

4. **Probar CRUD**
```
http://tu-dominio-aws/usuarios/
http://tu-dominio-aws/productos/
http://tu-dominio-aws/ventas/
```

---

## 📝 INFORMACIÓN PARA ENTREGA

**Completar y enviar:**

```
URL DEL PROYECTO DESPLEGADO:
http://___________________________

CREDENCIALES DE ACCESO:
Usuario: admin
Contraseña: admin123

REPOSITORIO GITHUB:
https://github.com/PandaAkiraNakai/GM-Express

URLS PRINCIPALES:
- Inicio: http://__________/
- Login: http://__________/login/
- Dashboard: http://__________/dashboard/
- Usuarios: http://__________/usuarios/
- Productos: http://__________/productos/
- Ventas: http://__________/ventas/

FECHA DE DESPLIEGUE:
___________ de noviembre de 2025

TIPO DE DESPLIEGUE EN AWS:
[ ] Elastic Beanstalk
[ ] EC2
[ ] Lightsail
```

---

## 🆘 SOLUCIÓN DE PROBLEMAS COMUNES

### Error: "DisallowedHost"
```python
# En settings.py
ALLOWED_HOSTS = ['*']  # Temporalmente
```

### Error: "No module named 'gmexpress'"
```bash
# Verificar PYTHONPATH
export PYTHONPATH=/home/ubuntu/GM-Express:$PYTHONPATH
```

### Error: "Static files not found"
```bash
python manage.py collectstatic --noinput
```

### Puerto 8000 no accesible
```bash
# Verificar firewall AWS Security Group
# Agregar regla: Custom TCP 8000, 0.0.0.0/0
```

---

## 📞 CONTACTO Y SOPORTE

**Documentación:**
- Django Deployment: https://docs.djangoproject.com/en/5.2/howto/deployment/
- AWS Elastic Beanstalk: https://aws.amazon.com/elasticbeanstalk/
- AWS EC2: https://aws.amazon.com/ec2/

**Repositorio:**
- https://github.com/PandaAkiraNakai/GM-Express

---

## ✨ RECOMENDACIONES FINALES

1. **Usar Elastic Beanstalk** para despliegue más rápido
2. **Documentar la URL** inmediatamente después del despliegue
3. **Hacer backup** de la base de datos antes de desplegar
4. **Probar todas las funcionalidades** después del despliegue
5. **Verificar logs** en caso de errores

---

**NOTA:** Esta guía asume conocimientos básicos de AWS. Para asistencia adicional, consultar la documentación oficial de AWS o solicitar ayuda al docente.

**¡Éxito en tu despliegue! 🚀**
