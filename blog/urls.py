from django.urls import path

from .views import BlogListView, blog_detail

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='index'),
    path('<int:id>/', blog_detail, name='blog_detail'),
]
