# 📋 INSTRUCCIONES PARA MIGRAR A MYSQL

## PASO 1: Crear Base de Datos en phpMyAdmin

1. Abre phpMyAdmin
2. Click en "Nueva" (New)
3. Nombre de la base de datos: `gmexpress`
4. Cotejamiento: `utf8mb4_unicode_ci`
5. Click "Crear"

---

## PASO 2: Configurar Django para MySQL

Edita el archivo `gmexpress/settings.py`:

```python
# Reemplaza la sección DATABASES con:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gmexpress',
        'USER': 'root',  # Tu usuario MySQL
        'PASSWORD': '',  # Tu contraseña MySQL
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        }
    }
}
```

---

## PASO 3: Instalar Driver MySQL

Abre PowerShell en la carpeta del proyecto:

```powershell
# Opción 1 (recomendada)
pip install pymysql

# Opción 2 (alternativa)
pip install mysqlclient
```

Si usas pymysql, edita `gmexpress/__init__.py` y agrega al inicio:

```python
import pymysql
pymysql.install_as_MySQLdb()
```

---

## PASO 4: Exportar Datos de SQLite

En PowerShell:

```powershell
cd "C:\Users\savka\OneDrive - INACAP\Escritorio\Backend\GM-Express"

# Activar entorno virtual
venv\Scripts\activate

# Exportar datos
python manage.py dumpdata --exclude auth.permission --exclude contenttypes --indent 2 > datos_backup.json
```

---

## PASO 5: Crear Tablas en MySQL

```powershell
python manage.py migrate
```

---

## PASO 6: Importar Datos

```powershell
python manage.py loaddata datos_backup.json
```

---

## PASO 7: Crear Superusuario

```powershell
python manage.py createsuperuser
```

Usuario: `admin`
Contraseña: `admin123`

---

## PASO 8: Verificar

```powershell
python manage.py runserver
```

Accede a: `http://127.0.0.1:8000/admin/`

---

## ⚠️ IMPORTANTE:

**Para la evaluación NO es necesario cambiar a MySQL.**

SQLite ya funciona perfectamente y cumple todos los requisitos.

Solo cambia a MySQL si:
- El profesor lo requiere explícitamente
- Necesitas desplegar en producción con alto tráfico
- Quieres aprender sobre MySQL

**Recomendación: Mantén SQLite para la entrega de hoy (18:30).**

---

## 🔙 Revertir a SQLite

Si algo sale mal, simplemente cambia en `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Y reinicia el servidor.
