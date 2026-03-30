from django.urls import path

from .views import CursosDetailView, CursosListView

app_name = 'courses'

urlpatterns = [
    path('', CursosListView.as_view(), name='index'),
    path('<int:id>/', CursosDetailView.as_view(), name='courses_detail'),
]
