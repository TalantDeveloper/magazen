from django.contrib import admin
from .models import Magazen, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class MagazenAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'file', 'created_at')
    list_display_links = ('id', 'name', 'image', 'file', 'created_at')
    search_fields = ('id', 'name', 'image', 'file', 'created_at')
    list_filter = ('name', 'file')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Magazen, MagazenAdmin)
