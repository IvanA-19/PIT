from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'project_name', 'date_added']
    list_display_links = ['project_name']
    search_fields = ['project_name']
    prepopulated_fields = {"project_slug": ('project_name', )}
    ordering = ['id', 'date_added']


class ProjectPhotoAdmin(admin.ModelAdmin):
    list_display = ['project', 'get_html_photo']
    list_display_links = ['project']
    search_fields = ['project']
    ordering = ['project']
    readonly_fields = ('get_html_photo',)

    def get_html_photo(self, object):
        return mark_safe(f'<img src="{object.photo.url}", width="50">')

    get_html_photo.short_description = 'Фото'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'theme', 'user', 'get_html_photo']
    list_display_links = ['theme']
    search_fields = ['theme']
    readonly_fields = ('get_html_photo', )

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}", width="50">')

    get_html_photo.short_description = 'Фото'


admin.site.register(models.Projects, ProjectsAdmin)
admin.site.register(models.ProjectPhoto, ProjectPhotoAdmin)
admin.site.register(models.Order, OrderAdmin)
