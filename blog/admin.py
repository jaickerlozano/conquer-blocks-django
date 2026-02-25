from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostResourece(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'pk', 'show_home', 'author', 'created_at')