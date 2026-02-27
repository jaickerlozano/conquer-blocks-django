from django.shortcuts import render, redirect  
from .models import Course
from django.contrib.auth.decorators import login_required

# Create your views here.

# Vista para listar todos los cursos.
# @login_required: Decorador que obliga al usuario a estar logueado para acceder a esta vista.
@login_required
def cursos_list(request):
    # Obtiene todos los objetos Course de la base de datos.
    courses = Course.objects.all()
    # Crea el contexto (datos) que se pasará al template.
    context = {
        'courses': courses,
    }
    # Renderiza el template 'courses/courses_list.html' con el contexto dado.
    return render(request, 'courses/courses_list.html', context)

# Vista para ver el detalle de un curso específico.
# También protegemos el detalle del curso.
@login_required
def cursos_detail(request, id):
    # Obtiene un único curso filtrando por su clave primaria (pk) que es el id.
    course = Course.objects.get(pk=id)
    context = {
        'course': course,
    }
    return render(request, 'courses/courses_detail.html', context)