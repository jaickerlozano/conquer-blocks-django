from django.urls import path, include
from .views import blog_list, blog_detail

app_name = 'blog'

urlpatterns = [
    path('', blog_list, name='index'),
    path('<int:id>/', blog_detail, name='blog_detail'),
]