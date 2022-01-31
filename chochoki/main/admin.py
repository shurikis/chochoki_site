from django.contrib import admin

from .models import *


class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_create', 'is_published')
    list_display_links = ('name',)
    search_fields = ('name', 'desc')
    list_editable = ('is_published',)


admin.site.register(Game, GameAdmin)
admin.site.register(User)
