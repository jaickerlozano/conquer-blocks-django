# Conquer Blocks Django Platform

Plataforma educativa desarrollada en Django, migrada y evolucionada desde una versión estática en HTML (ConquerBlocks). Este proyecto permite la gestión dinámica de cursos, un blog y contenido multimedia.

## Características Principales

- **Gestión de Cursos (`courses`):** Sistema para crear y administrar cursos con títulos, imágenes de portada y temarios (PDF).
- **Contenido Enriquecido:** Integración de **CKEditor** para la edición avanzada de descripciones y contenidos de los cursos.
- **Blog (`blog`):** Sección dedicada a artículos y noticias.
- **Web Principal (`main_web`):** Landing page y páginas estáticas del sitio.
- **Gestión de Imágenes:** Uso de `django-thumbnails` para el redimensionamiento y optimización de imágenes.

## Tecnologías Utilizadas

- **Python** (3.12)
- **Django** (Framework Web)
- **SQLite** (Base de datos por defecto para desarrollo)
- **CKEditor** (Editor de texto enriquecido WYSIWYG)
- **Django Extensions & Debug Toolbar** (Herramientas de desarrollo)

## Requisitos Previos

Asegúrate de tener instalado:
- Python 3.x
- Git

## Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   cd conquer-blocks-django
   ```

2. **Crear y activar un entorno virtual:**
   ```bash
   python -m venv env
   
   # En Windows:
   .\env\Scripts\activate
   # En macOS/Linux:
   source env/bin/activate
   ```

3. **Instalar dependencias:**
   *(Si aún no has generado el archivo requirements.txt, puedes omitir este paso o instalar Django manualmente)*
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplicar migraciones a la base de datos:**
   ```bash
   python manage.py migrate
   ```

5. **Crear un superusuario (para acceder al panel de administración):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar el servidor:**
   ```bash
   python manage.py runserver
   ```

## Uso

Una vez encendido el servidor, puedes acceder a:
- **Sitio Web:** `http://127.0.0.1:8000/`
- **Panel de Administración:** `http://127.0.0.1:8000/admin/` (Ingresa con el superusuario creado en el paso 5).
