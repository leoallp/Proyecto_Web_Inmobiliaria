import json
from django.core.management.base import BaseCommand
from arriendo_app.models import Region, Comuna

class Command(BaseCommand):
    # Define un mensaje de ayuda que describe lo que hace este comando.
    help = 'Populate database with regions and comunas'

    # El método handle es el punto de entrada para los comandos de administración personalizados.
    def handle(self, *args, **kwargs):
        # Abre el archivo JSON que contiene las regiones y comunas.
        with open('json/regiones_comunas.json', encoding='utf-8') as file:
            # Carga el contenido del archivo JSON en una variable de datos.
            data = json.load(file)
            # Itera sobre cada entrada en los datos JSON.
            for entry in data:
                # Obtiene el nombre de la región de la entrada actual.
                region_name = entry['region']
                # Obtiene la lista de comunas de la entrada actual.
                comunas = entry['comunas']
                # Crea o obtiene la región en la base de datos.
                # Si la región ya existe, la obtiene. Si no, la crea.
                region, created = Region.objects.get_or_create(nombre=region_name)
                # Itera sobre cada nombre de comuna en la lista de comunas.
                for comuna_name in comunas:
                    # Crea o obtiene la comuna en la base de datos,
                    # asociándola con la región correspondiente.
                    # Si la comuna ya existe, la obtiene. Si no, la crea.
                    Comuna.objects.get_or_create(nombre=comuna_name, region=region)
        # Imprime un mensaje de éxito en la consola.
        self.stdout.write(self.style.SUCCESS('Regiones y comunas cargados exitosamente'))
