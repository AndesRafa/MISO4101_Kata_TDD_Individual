from django.contrib import admin
from .models import TiposDeServicio, Trabajador

# Register your models here.
class TiposDeServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos')

admin.site.register(TiposDeServicio, TiposDeServicioAdmin)
admin.site.register(Trabajador, TrabajadorAdmin)
