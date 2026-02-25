from django.urls import path, include
from .views import cursos_list, cursos_detail

app_name = 'courses'

urlpatterns = [
    path('', cursos_list, name='index'),
    path('<int:id>/', cursos_detail, name='courses_detail'),
]