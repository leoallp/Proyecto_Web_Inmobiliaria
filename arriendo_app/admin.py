from django.contrib import admin
from.models import Region, Comuna, Usuario, TipoUsuario, Inmueble, TipoInmueble, Pais
# Register your models here.
admin.site.register(Pais)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(TipoInmueble)
admin.site.register(TipoUsuario)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'disponibilidad', 'comuna', 'region']
    
admin.site.register(Inmueble, InmuebleAdmin)

admin.site.register(Usuario)
