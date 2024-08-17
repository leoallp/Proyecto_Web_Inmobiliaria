# Proyecto_Web_Inmobiliaria

# SUGERENCIAS: 
# pip install -r ev_inmobiliaria.txt              -> comando para instalar todos los paquetes listados en ev_inmobiliaria.txt > 

# setting.py ya configurado para usar bbdd postgres; Verificar coincidencia del "NAME" y "PASSWORD" con la bbdd postgres a utilizar
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "inmobiliaria",
        "USER": "postgres",
        "PASSWORD": "Admin1234",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

# Loaddata
# para poblar los modelos pais, region y comuna usando el json disponible usar el siguiente comando; 
# python manage.py loaddata json/regiones_comunas_chile.json  
# previamente verificar Env activado y estar ubicado en la carpeta raiz proy_inmobiliaria