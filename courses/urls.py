from django.urls import path

from .views import cursos_detail, cursos_list

app_name = 'courses'

urlpatterns = [
    path('', cursos_list, name='index'),
    path('<int:id>/', cursos_detail, name='courses_detail'),
]
