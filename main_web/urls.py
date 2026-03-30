from django.urls import path

from .views import (
    ContactoView,
    HomeView,
    HomeView2,
    QuienesSomosView,
    RegistroView,
    contacto_view,
    login_view,
    logout_view,
    registro_view,
)

app_name = 'main_web'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('index2/', HomeView2.as_view(), name='index2'),
    path('quienes-somos/', QuienesSomosView.as_view(), name='quienes_somos'),
    path('registro/', registro_view, name='registro'),
    path('registro/ccbv/', RegistroView.as_view(), name='registro_ccbv'),
    # Rutas para autenticación
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('contacto/', contacto_view, name='contacto'),
    path('contacto/ccbv/', ContactoView.as_view(), name='contacto_ccbv'),
]
