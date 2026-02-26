from django.contrib import admin
from .models import Contact

# Register your models here.

# Registra el modelo Contact en el panel de administración usando el decorador.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # Define qué campos se mostrarán como columnas en la lista de contactos del admin.
    list_display = ('name', 'contactado', 'email', 'created_at')
    list_filter = ('contactado', 'created_at')  # Agrega filtros para los campos 'contactado' y 'created_at'.
    search_fields = ('name', 'email')  # Agrega un campo de búsqueda para los campos 'name' y 'email'.
    ordering = ('-created_at',) # Ordena los contactos por fecha de creación de forma descendente (los más recientes primero).