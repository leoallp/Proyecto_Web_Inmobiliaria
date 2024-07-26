import os, django, time

os.environ.setdefault("DJANGO_SETTINGS_MODULE","proy_inmobiliaria.settings")
django.setup()

from arriendo_app.models import Inmueble, Region, Comuna

def obtener_inmuebles_comuna(comuna_nombre):
    select = '''
            selec inmueble.id, inmueble.nombre,
            comuna.nombre as comuna, region.nombre as region
            from arriendo_app inmueble
            inner join arriendo_app_comuna comuna
            on inmueble.comuna_id = comuna.id
            inner join arriendo_app_region region
            on inmueble.region_id = region.id
            where comuna.nombre LIKE '%'''+str(comuna_nombre)+'''%'
            '''
    data_inmuebles = Inmueble.objects.raw(select)
    
    archivo = open("inmueble_comuna.txt", "w")
    
    for inmueble in data_inmuebles:
        archivo.write(inmueble.id + '-' + inmueble.nombre + '\n')
        
    archivo.close()
    
    
def obtener_inmueble(nombre, descripcion):
    lista_inmuebles = Inmueble.objects.filter(nombre__contains=nombre).filter(descripcion__contains=descripcion)
    
    archivo = open("inmueble_nombre_des.txt", "w")
    
    for inmueble in lista_inmuebles:
        archivo.write(inmueble + '\n')
        
    archivo.close()
    
    

    
    
    
    
    
    
    





