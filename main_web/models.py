from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    name = models.CharField(
        verbose_name="Nombre",
        max_length=100
    )
    email = models.EmailField(
        verbose_name="Email"
    )
    message = models.TextField(
        verbose_name="Mensaje que ha dejado en la web"
    )
    created_at = models.DateTimeField(
        verbose_name="Fecha de creación",
        default=timezone.now
    )
    contactado = models.BooleanField(
        verbose_name="¿El contacto ha sido atendido?",
        default=False
    )

    def __str__(self):
        return f"Contacto de {self.name} ({self.email})"