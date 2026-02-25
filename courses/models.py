from django.db import models
from django.utils import timezone
from thumbnails.fields import ImageField
from ckeditor.fields import RichTextField

# Create your models here.
# Definición del modelo Course, que representa un curso en la base de datos.
class Course(models.Model):
    # Campo de texto corto para el título.
    title = models.CharField(
        verbose_name='Título del curso', # Nombre legible en el admin.
        max_length=200,
    )
    # Campo de texto enriquecido (gracias a CKEditor) para el contenido.
    content = RichTextField(
        verbose_name='Contenido del curso',
    )
    # Campo para URLs.
    call_link = models.URLField(
        verbose_name='Enlace de inscripción',
    )
    # Fecha de creación. 'default=timezone.now' asigna la fecha/hora actual automáticamente al crear.
    created_at = models.DateTimeField(
        verbose_name='Fecha y hora de creación',
        default=timezone.now,
    )
    # Booleano para decidir si mostrar este curso en la home.
    show_home = models.BooleanField(
        verbose_name='Mostrar en la página de inicio',
        default=False,
    )
    # Campo para subir archivos (PDFs, etc.).
    toc = models.FileField(
        verbose_name='Temario',
        upload_to='courses/toc/', #-> Con esta línea le decimos a Django que los archivos subidos a este campo se guarden en la carpeta 'media/courses/toc/'
        null=True, # Permite que el campo sea NULL en la base de datos.
        blank=True, # Permite que el campo se deje vacío en los formularios (como el admin).
    )
    # Campo para subir imágenes, con soporte para miniaturas si se usa la librería adecuada.
    course_image = ImageField(
        verbose_name='Portada del curso',
        upload_to='courses/images/', #-> Con esta línea le decimos a Django que los archivos subidos a este campo se guarden en la carpeta 'media/courses/images/'
        null=True,
        blank=True,
    )

    # Método mágico para representar el objeto como cadena (útil en el admin y shell).
    def __str__(self):
        return self.title