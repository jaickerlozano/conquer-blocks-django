from django.contrib import admin

from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'call_link', 'show_home', 'created_at', 'has_file')
    list_filter = ('show_home', 'created_at')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)
    list_editable = ('show_home',)
    list_per_page = 25
    readonly_fields = ('created_at',)

    @admin.display(boolean=True, description='Temario')
    def has_file(self, obj):
        return bool(obj.toc)
