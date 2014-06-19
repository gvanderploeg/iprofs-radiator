import uuid
from models import Playlist, Device, Url
from django.contrib import admin

class UrlInline(admin.StackedInline):
    model = Url
    extra = 3

class DeviceAdmin(admin.ModelAdmin):
    readonly_fields = ['uuid']

class PlaylistAdmin(admin.ModelAdmin):
    inlines = [UrlInline]

admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Device, DeviceAdmin)
