"""conquer_blocks_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Incluye las URLs de la app 'main_web'. El namespace permite referirse a estas URLs como 'main_web:nombre_url'.
    path('', include('main_web.urls', namespace='main_web')),
    # Incluye las URLs de la app 'blog'.
    path('blog/', include('blog.urls', namespace='blog')),
    # Incluye las URLs de la app 'courses'.
    path('cursos/', include('courses.urls', namespace='courses')),
    # URL para el panel de administración de Django.
    path('admin/', admin.site.urls),
] + debug_toolbar_urls() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# La línea anterior añade las URLs del debug toolbar y configura Django para servir archivos media en desarrollo.
