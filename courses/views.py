from django.shortcuts import render
from .models import Course

# Create your views here.

# Vista para listar todos los cursos.
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
def cursos_detail(request, id):
    # Obtiene un único curso filtrando por su clave primaria (pk) que es el id.
    course = Course.objects.get(pk=id)
    context = {
        'course': course,
    }
    return render(request, 'courses/courses_detail.html', context)