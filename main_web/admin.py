from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contactado', 'created_at')
    list_filter = ('contactado', 'created_at')
    search_fields = ('name', 'email', 'message')
    ordering = ('-created_at',)
    list_editable = ('contactado',)
    list_per_page = 25

    actions = ['mark_as_contacted', 'mark_as_not_contacted']

    @admin.action(description='Marcar como contactado')
    def mark_as_contacted(self, request, queryset):
        queryset.update(contactado=True)

    @admin.action(description='Marcar como no contactado')
    def mark_as_not_contacted(self, request, queryset):
        queryset.update(contactado=False)
