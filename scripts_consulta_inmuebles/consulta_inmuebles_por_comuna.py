import os
import django
from django.conf import settings

# Configura Django para que pueda acceder a la base de datos
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proy_inmobiliaria.settings')
django.setup()

from arriendo_app.models import Inmueble, Comuna

# Consulta los inmuebles disponibles para arriendo, ordenados por comunas
inmuebles_por_comuna = {}

for comuna in Comuna.objects.all():
    inmuebles = Inmueble.objects.filter(comuna=comuna, disponibilidad=True).values('nombre', 'descripcion')
    if inmuebles.exists():
        inmuebles_por_comuna[comuna.nombre] = list(inmuebles)

# Guarda los resultados en un archivo TXT
with open('inmuebles_por_comuna.txt', 'w', encoding='utf-8') as file:
    for comuna, inmuebles in inmuebles_por_comuna.items():
        file.write(f"Comuna: {comuna}\n")
        for inmueble in inmuebles:
            file.write(f"  Nombre: {inmueble['nombre']}\n")
            file.write(f"  Descripción: {inmueble['descripcion']}\n")
        file.write("\n")

print("Archivo inmuebles_por_comuna.txt generado con éxito.")


