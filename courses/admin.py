from django.contrib import admin
from .models import Course

# Registra el modelo Course en el panel de administración usando el decorador.
@admin.register(Course)
class CourseResourece(admin.ModelAdmin):
    # Especifica el modelo asociado (aunque es redundante con el decorador, a veces se usa).
    model = Course
    # Define qué campos se mostrarán como columnas en la lista de cursos del admin.
    list_display = ('title', 'show_home', 'content', 'call_link', 'created_at')