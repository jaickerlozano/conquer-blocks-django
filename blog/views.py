from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ['-created_at']


def blog_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {
        'post': post,
    }
    return render(request, 'blog/blog_detail.html', context)
