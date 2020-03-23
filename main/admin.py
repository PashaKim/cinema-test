from django.contrib import admin
from .models import Menu, MenuElement


class MenuElementInLines(admin.TabularInline):
    model = MenuElement
    extra = 2
    readonly_fields = ('created', 'updated')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name','elements', 'created', 'updated')
    readonly_fields = ('created', 'updated')
    inlines = [MenuElementInLines]


@admin.register(MenuElement)
class MenuElement(admin.ModelAdmin):
    list_display = ('menu', 'name', 'url', 'created', 'updated')
    list_filter = ('menu',)
    readonly_fields = ('created', 'updated')

