from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Post


# Create your views here.
def blog_list(request):
    all_post = Post.objects.all()
    context = {
        'posts': all_post,
    }
    return render(request, 'blog/blog_list.html', context)

class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog_list_ccbv.html'
    context_object_name = 'posts'

def blog_detail(request, id):
    post = Post.objects.get(pk=id)
    context = {
        'post': post,
    }
    return render(request, 'blog/blog_detail.html', context)
