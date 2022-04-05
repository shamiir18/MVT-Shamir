from django.contrib import admin

from .models import Familia

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'relacion', 'edad', 'fecha_nacimiento')


admin.site.register(Familia,FamiliaAdmin)