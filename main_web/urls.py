from django.urls import path

from .views import (
    ContactoView,
    HomeView,
    HomeView2,
    LoginView,
    QuienesSomosView,
    RegistroView,
    logout_view,
)

app_name = 'main_web'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('index2/', HomeView2.as_view(), name='index2'),
    path('quienes-somos/', QuienesSomosView.as_view(), name='quienes_somos'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('contacto/', ContactoView.as_view(), name='contacto'),
]
