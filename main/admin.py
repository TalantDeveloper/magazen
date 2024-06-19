from django.contrib import admin
from .models import Magazen


class MagazenAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'file', 'created_at')
    list_display_links = ('id', 'name', 'image', 'file', 'created_at')
    search_fields = ('id', 'name', 'image', 'file', 'created_at')
    list_filter = ('name', 'file')


admin.site.register(Magazen, MagazenAdmin)
