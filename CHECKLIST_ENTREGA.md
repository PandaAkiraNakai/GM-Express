# ✅ CHECKLIST DE ENTREGA - EVALUACIÓN GM EXPRESS
## Programación Back End - INACAP
## Fecha Límite: 10 de noviembre de 2025, 18:30 hrs

---

## 📋 ANTES DE LA ENTREGA

### **1. VERIFICACIÓN LOCAL** ✅

#### Servidor Local Funcional
- [ ] `python manage.py runserver` ejecuta sin errores
- [ ] http://127.0.0.1:8000/ carga correctamente
- [ ] Login funciona (admin/admin123)
- [ ] Dashboard carga con estadísticas
- [ ] Todas las páginas CRUD son accesibles

#### Formularios y Validaciones
- [ ] Formularios de usuarios funcionan
- [ ] Formularios de productos funcionan
- [ ] Formularios de categorías funcionan
- [ ] Formularios de ventas funcionan
- [ ] Formularios de servicios funcionan
- [ ] Validaciones muestran mensajes de error apropiados
- [ ] No se permite fecha de venta futura
- [ ] No se permite duplicar RUT/correo
- [ ] Stock se valida correctamente

#### Operaciones CRUD
- [ ] **Usuarios**: Crear, Leer, Actualizar, Eliminar ✓
- [ ] **Tipos de Usuario**: Crear, Leer, Actualizar, Eliminar ✓
- [ ] **Categorías**: Crear, Leer, Actualizar, Eliminar ✓
- [ ] **Productos**: Crear, Leer, Actualizar, Eliminar ✓
- [ ] **Ventas**: Crear, Leer, Actualizar, Eliminar ✓
- [ ] **Servicios**: Crear, Leer, Actualizar, Eliminar ✓

#### Autenticación
- [ ] Login redirige a dashboard
- [ ] Logout funciona y muestra mensaje
- [ ] Vistas CRUD requieren login
- [ ] Usuario no logueado es redirigido a login

---

### **2. DOCUMENTACIÓN COMPLETA** 📚

#### Archivos Requeridos
- [ ] `README.md` con instrucciones de instalación
- [ ] `requirements.txt` con todas las dependencias
- [ ] `RESUMEN_IMPLEMENTACION.md` (opcional pero útil)
- [ ] `GUIA_DESPLIEGUE_AWS.md` (opcional pero útil)
- [ ] `.github/copilot-instructions.md` (para referencia)

#### Contenido del README
- [ ] Descripción del proyecto
- [ ] Requisitos previos
- [ ] Pasos de instalación (1-2-3-4-5)
- [ ] Comando para ejecutar: `python manage.py runserver`
- [ ] Credenciales de acceso documentadas
- [ ] URLs principales listadas
- [ ] Estructura del proyecto explicada

---

### **3. DESPLIEGUE EN AWS** 🚀

#### Preparación
- [ ] Cuenta AWS activa y funcionando
- [ ] Elegir método de despliegue (Elastic Beanstalk/EC2/Lightsail)
- [ ] Configurar `settings.py` para producción
- [ ] Actualizar `ALLOWED_HOSTS` con IP/dominio AWS
- [ ] Instalar `gunicorn` si usas EC2

#### Despliegue Realizado
- [ ] Proyecto desplegado en AWS
- [ ] URL pública accesible desde navegador
- [ ] Login funciona en producción
- [ ] Dashboard carga correctamente
- [ ] Al menos 3 operaciones CRUD probadas en producción

#### URLs de Producción Funcionando
- [ ] Página de inicio
- [ ] Login
- [ ] Dashboard
- [ ] Lista de usuarios
- [ ] Lista de productos
- [ ] Lista de ventas

---

### **4. MATERIAL A ENTREGAR** 📦

#### Código Fuente
- [ ] Repositorio GitHub actualizado
- [ ] Todos los commits pusheados
- [ ] Archivo `.gitignore` configurado
- [ ] README.md en la raíz del proyecto

#### Documentación de Entrega
- [ ] URL del proyecto en AWS (anotar aquí):
  ```
  http://________________________________
  ```

- [ ] Usuario y contraseña de prueba:
  ```
  Usuario: admin
  Contraseña: admin123
  ```

- [ ] URL del repositorio GitHub:
  ```
  https://github.com/PandaAkiraNakai/GM-Express
  ```

- [ ] Tipo de despliegue usado:
  ```
  [ ] Elastic Beanstalk
  [ ] EC2
  [ ] Lightsail
  ```

---

## 📤 PROCESO DE ENTREGA

### **PASO 1: Preparar el Paquete de Entrega**

Crear un archivo de texto `ENTREGA_GM_EXPRESS.txt` con:

```
========================================
EVALUACIÓN - PROGRAMACIÓN BACK END
PROYECTO: GM EXPRESS
ESTUDIANTE: [TU NOMBRE COMPLETO]
FECHA: 10 de noviembre de 2025
========================================

1. URL DEL PROYECTO DESPLEGADO EN AWS:
http://________________________________

2. CREDENCIALES DE ACCESO:
Usuario: admin
Contraseña: admin123

3. REPOSITORIO GITHUB:
https://github.com/PandaAkiraNakai/GM-Express

4. URLS PRINCIPALES DEL SISTEMA:

PÁGINAS PÚBLICAS:
- Inicio: http://[TU-URL]/
- Catálogo: http://[TU-URL]/catalogo/
- Login: http://[TU-URL]/login/

PÁGINAS PROTEGIDAS (requieren login):
- Dashboard: http://[TU-URL]/dashboard/
- Usuarios: http://[TU-URL]/usuarios/
- Productos: http://[TU-URL]/productos/
- Categorías: http://[TU-URL]/categorias/
- Ventas: http://[TU-URL]/ventas/
- Servicios: http://[TU-URL]/servicios/
- Admin Django: http://[TU-URL]/admin/

5. FUNCIONALIDADES IMPLEMENTADAS:
✅ Sistema de autenticación (login/logout)
✅ CRUD completo de Usuarios
✅ CRUD completo de Tipos de Usuario
✅ CRUD completo de Productos
✅ CRUD completo de Categorías
✅ CRUD completo de Ventas
✅ CRUD completo de Servicios
✅ Validaciones de formato (RUT, email, teléfono)
✅ Validaciones de negocio (fechas, duplicados, stock)
✅ Formularios con mensajes de error
✅ Base de datos configurada
✅ Código documentado

6. TECNOLOGÍAS UTILIZADAS:
- Django 5.2.7
- Python 3.11+
- SQLite (desarrollo) / MySQL (producción opcional)
- Bootstrap 5
- AWS [Elastic Beanstalk/EC2/Lightsail]

7. ARCHIVOS IMPORTANTES:
- README.md: Instrucciones de instalación
- requirements.txt: Dependencias del proyecto
- RESUMEN_IMPLEMENTACION.md: Resumen técnico
- GUIA_DESPLIEGUE_AWS.md: Guía de despliegue

8. NOTAS ADICIONALES:
[Agregar cualquier información relevante]

========================================
DECLARACIÓN:
Declaro que este trabajo es de mi autoría
y ha sido desarrollado siguiendo las 
instrucciones de la evaluación.

Firma: ______________________
Fecha: 10/11/2025
========================================
```

---

### **PASO 2: Comprimir el Código Fuente**

```bash
# En Windows PowerShell (carpeta del proyecto)
Compress-Archive -Path * -DestinationPath GM-Express-Codigo.zip

# Asegurarse de incluir:
# - Todos los archivos .py
# - requirements.txt
# - README.md
# - templates/
# - static/
# - manage.py
# - db.sqlite3 (con datos de prueba)
```

---

### **PASO 3: Subir a AWS (según instrucciones del docente)**

- [ ] Proyecto desplegado y funcionando
- [ ] URL pública accesible
- [ ] Probar login desde navegador externo
- [ ] Verificar al menos 3 funciones CRUD

---

### **PASO 4: Envío Final**

#### Entregar antes de las 18:30 hrs del 10/11/2025:

1. **Archivo de texto** `ENTREGA_GM_EXPRESS.txt` con toda la información
2. **Código fuente** comprimido `GM-Express-Codigo.zip`
3. **Captura de pantalla** del sitio funcionando en AWS (opcional)
4. **Link del repositorio** GitHub

#### Método de Entrega:
- [ ] A través de AWS (según instrucciones del docente)
- [ ] No por correo electrónico
- [ ] No en computador personal

---

## ⚠️ ADVERTENCIAS IMPORTANTES

### **NO SE ACEPTARÁ:**
- ❌ Entregas posteriores a las 18:30 hrs
- ❌ Entregas por correo electrónico
- ❌ Entregas en computadores personales
- ❌ Proyectos que no ejecuten con `python manage.py runserver`
- ❌ Proyectos sin README.md
- ❌ Proyectos sin requirements.txt

### **CAUSALES DE NOTA 1.0:**
- ❌ Similitud >20% con otra entrega
- ❌ Sospecha de uso de IA sin desarrollo propio
- ❌ Proyecto no funcional
- ❌ No poder explicar el código durante la revisión

---

## 🎯 AUTOEVALUACIÓN FINAL

Antes de entregar, responde honestamente:

- [ ] ¿El proyecto ejecuta sin errores en mi computador?
- [ ] ¿Está desplegado y funciona en AWS?
- [ ] ¿Puedo explicar cómo funciona cada parte del código?
- [ ] ¿Entiendo las validaciones que implementé?
- [ ] ¿Probé todas las funciones CRUD?
- [ ] ¿La documentación está completa?
- [ ] ¿Las credenciales están documentadas?
- [ ] ¿Tengo el archivo de entrega preparado?

**Si todas las respuestas son SÍ, estás listo para entregar. ✅**

---

## 📊 EVALUACIÓN ESPERADA

### Criterios (según rúbrica oficial):

1. **Configuración BD (2.1.1)**: ✅ SQLite configurada
2. **Admin Django (2.1.2)**: ✅ Funcional en /admin/
3. **CRUD (2.1.3)**: ✅ Todas las entidades
4. **Seguridad (2.1.4)**: ✅ Login + @login_required

### Puntaje Esperado:
- Formularios completos: 25%
- Validaciones: 25%
- CRUD funcional: 30%
- Autenticación: 10%
- Documentación: 10%

**TOTAL ESPERADO: 100% (Nota 7.0)** 🎉

---

## ✨ ÚLTIMA VERIFICACIÓN ANTES DE ENVIAR

```bash
# En la carpeta del proyecto, ejecutar:
python manage.py runserver

# Abrir navegador y probar:
1. http://127.0.0.1:8000/ → Debe cargar la página de inicio
2. http://127.0.0.1:8000/login/ → Probar login con admin/admin123
3. http://127.0.0.1:8000/dashboard/ → Debe mostrar estadísticas
4. http://127.0.0.1:8000/usuarios/ → Debe mostrar lista
5. http://127.0.0.1:8000/usuarios/crear/ → Probar crear usuario
6. Probar validaciones (RUT inválido, fecha futura, etc.)
7. Cerrar sesión y verificar redirección

# Si TODO funciona correctamente:
✅ LISTO PARA ENTREGAR
```

---

**💡 CONSEJO FINAL:**

**Entrega con tiempo de sobra (antes de las 18:00). No esperes hasta el último minuto por si hay problemas con AWS o la conexión.**

---

## 📞 EN CASO DE PROBLEMAS

Si encuentras algún problema:

1. **Revisar logs de error**
2. **Verificar settings.py**
3. **Comprobar migraciones**
4. **Revisar GUIA_DESPLIEGUE_AWS.md**
5. **Consultar con docente (con tiempo de anticipación)**

---

**¡MUCHO ÉXITO EN TU EVALUACIÓN! 🚀✨**

---

*Checklist creado para GM Express - Evaluación Programación Back End - INACAP - Noviembre 2025*
