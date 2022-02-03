from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_create', 'get_html_img', 'is_published', 'get_stage')
    list_display_links = ('name',)
    search_fields = ('name', 'desc')
    list_editable = ('is_published',)
    fields = ('name', 'desc', 'is_published', 'html', 'stage', 'img', 'get_html_img', 'time_create', 'time_update', 'token', 'get_token')
    readonly_fields = ('get_html_img', 'time_create', 'time_update', 'get_token')

    def add_view(self, request, form_url='', extra_context=None):
        a = {}
        for i in dict(request.POST).items():
            a[i[0]] = i[1][0]
        request.POST = a
        request.POST['token'] = base64.b64encode(os.urandom(20)).decode().replace('=', '').replace('/', '').replace('\\', '')
        print(request.POST)
        return super(GameAdmin, self).add_view(request, form_url, extra_context)
    
    def change_view(self, request, object_id, form_url='', extra_context=None):
        game = Game.objects.get(id=object_id)
        a = {}
        for i in dict(request.POST).items():
            a[i[0]] = i[1][0]
        request.POST = a
        request.POST['token'] = game.token
        return super(GameAdmin, self).change_view(request, object_id, form_url, extra_context)

    def get_stage(self, obj: Game):
        return obj.stage.name[0].upper() + obj.stage.name[1:]

    def get_html_img(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width=30>')

    def get_token(self, obj: Game):
        return mark_safe(f'<!---<p>{obj.token}</p>---> <button><a href="/games/{obj.name}/token/{obj.token}">regenerate token</a></button>')

    get_html_img.short_description = 'Image'
    get_token.short_description = 'Token'


admin.site.register(Game, GameAdmin)
admin.site.register(User)
admin.site.register(Stage)
