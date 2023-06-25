from django.contrib import admin

from ordenamiento.models import Barrio, Parroquia

class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo')
    search_fields = ('nombre', 'tipo')


admin.site.register(Parroquia, ParroquiaAdmin)

class BarrioAdmin(admin.ModelAdmin): 
    list_display = ('nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios', 'parroquia')
    
    raw_id_fields = ('parroquia',)

admin.site.register(Barrio, BarrioAdmin)
