from django.urls import path

from .views import BlogListView, blog_detail, blog_list

app_name = 'blog'

urlpatterns = [
    path('', blog_list, name='index'),
    path('<int:id>/', blog_detail, name='blog_detail'),
    path('ccbv/', BlogListView.as_view(), name='blog_list_ccbv'),
]
