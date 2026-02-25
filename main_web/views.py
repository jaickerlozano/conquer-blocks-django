from django.shortcuts import render
from courses.models import Course
from blog.models import Post


# Create your views here.
def home_view(request):
    # Contexto para la página de inicio.
    context = {
        # Filtra los cursos para mostrar solo los que tienen show_home=True.
        'courses': Course.objects.filter(show_home=True),
        # Filtra los posts para mostrar solo los que tienen show_home=True.
        'posts': Post.objects.filter(show_home=True),
    }
    return render(request, 'main_web/index.html', context)

def quienes_somos_view(request):
    return render(request, 'main_web/quienes_somos.html')

def registro_view(request):
    return render(request, 'main_web/registro.html')

def login_view(request):
    return render(request, 'main_web/login.html')

def contacto_view(request):
    return render(request, 'main_web/contacto.html')