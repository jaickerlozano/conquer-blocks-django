from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'show_home', 'created_at', 'content_preview')
    list_filter = ('show_home', 'created_at', 'author')
    search_fields = ('title', 'content', 'author')
    ordering = ('-created_at',)
    list_editable = ('show_home',)
    list_per_page = 25
    readonly_fields = ('created_at',)

    @admin.display(description='Contenido')
    def content_preview(self, obj):
        return obj.content[:100] + '...' if len(obj.content) > 100 else obj.content
