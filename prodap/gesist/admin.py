from django.contrib import admin
from .models import Servers, System_server, System, Sector
from django.contrib.admin import ModelAdmin, TabularInline, register

class SystemserverInLine(TabularInline):
    model = System_server
    extra = 1

@register(Sector)
class sectorAdmin(ModelAdmin):
    icon_name = 'check_circle'


@register(Servers)
class serverAdmin(ModelAdmin):
    icon_name = 'check_circle'
    search_fields = ('ip', 'sector')
    list_display = ('ip', 'sector')
    inlines = [SystemserverInLine]

@register(System)
class systemAdmin(ModelAdmin):
    icon_name = 'check_circle'
    list_display = ('system_name', 'responsible', 'server')
# Register your models here.
