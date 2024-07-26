import json
from django.core.management.base import BaseCommand
from arriendo_app.models import TipoInmueble

class Command(BaseCommand):
    help = 'Load predefined types of property into the database'

    def handle(self, *args, **kwargs):
        with open('json/tipos_inmueble.json', encoding='utf-8') as file:
            data = json.load(file)
            for entry in data:
                nombre = entry['nombre']
                TipoInmueble.objects.get_or_create(nombre=nombre)
        self.stdout.write(self.style.SUCCESS('Tipos de inmueble cargados exitosamente'))
