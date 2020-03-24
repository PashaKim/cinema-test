from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Menu, MenuElement, Film, News


class MenuElementInLines(admin.TabularInline):
    model = MenuElement
    extra = 2
    readonly_fields = ('created', 'updated')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'elements', 'created', 'updated')
    readonly_fields = ('created', 'updated')
    inlines = [MenuElementInLines]


# @admin.register(MenuElement)
# class MenuElement(admin.ModelAdmin):
#     list_display = ('menu', 'name', 'url', 'created', 'updated')
#     list_filter = ('menu',)
#     readonly_fields = ('created', 'updated')


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    fields = ('name', 'poster', 'image_tag', 'date_release','trailer_url', 'description', 'created', 'updated')
    list_display = ('name', 'image_tag', 'date_release', 'created', 'updated')
    readonly_fields = ('created', 'updated', 'image_tag')
    list_filter = ('date_release',)

    def image_tag(self, obj):
        return mark_safe(f'<img src="{obj.poster.url}" width="150" height="150" />')
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


@admin.register(News)
class FilmAdmin(admin.ModelAdmin):
    fields = ('name', 'image', 'image_tag', 'description', 'created', 'updated')
    list_display = ('name', 'image_tag', 'created', 'updated')
    readonly_fields = ('created', 'updated', 'image_tag')

    def image_tag(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="150" height="150" />')
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
