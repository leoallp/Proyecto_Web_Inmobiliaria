import os
import django
from django.conf import settings

# Configura Django para que pueda acceder a la base de datos
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proy_inmobiliaria.settings')
django.setup()

from arriendo_app.models import Inmueble, Region

# Consulta los inmuebles disponibles para arriendo, ordenados por regiones
inmuebles_por_region = {}

for region in Region.objects.all():
    inmuebles = Inmueble.objects.filter(region=region, disponibilidad=True).values('nombre', 'descripcion')
    if inmuebles.exists():
        inmuebles_por_region[region.nombre] = list(inmuebles)

# Guarda los resultados en un archivo TXT
with open('inmuebles_por_region.txt', 'w', encoding='utf-8') as file:
    for region, inmuebles in inmuebles_por_region.items():
        file.write(f"Región: {region}\n")
        for inmueble in inmuebles:
            file.write(f"  Nombre: {inmueble['nombre']}\n")
            file.write(f"  Descripción: {inmueble['descripcion']}\n")
        file.write("\n")

print("Archivo inmuebles_por_region.txt generado con éxito.")
