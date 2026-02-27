from django.urls import path, include
from .views import  (
    home_view, quienes_somos_view, registro_view, 
    login_view, contacto_view, logout_view
)

app_name = 'main_web'

urlpatterns = [
    path('', home_view, name='index'),
    path('quienes-somos/', quienes_somos_view, name='quienes_somos'),
    path('registro/', registro_view, name='registro'),
    # Rutas para autenticación
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('contacto/', contacto_view, name='contacto'),
]