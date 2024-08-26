# Proyecto_Web_Inmobiliaria  
![Indice](screenshots/index.png)

# ******** Sugerencias de instalación ********

# Requirements
Para instalar todos los paquetes listados en ev_inmobiliaria.txt usar:  
pip install -r ev_inmobiliaria.txt               

# Base de datos
setting.py ya configurado para usar bbdd postgres; Verificar coincidencia del "NAME" y "PASSWORD" con la bbdd postgres a utilizar

# Loaddata
Para poblar los modelos pais, region y comuna usando loaddata y el json disponible usar:  
python manage.py loaddata json/regiones_comunas_chile.json  

# Scritps de consulta de inmuebles
Los script de consulta de inmuebles por region y comuna son opcionales y van a depender si se hayan poblado dichos modelos, usar:  
python consulta_inmuebles_por_comuna.py  
python consulta_inmuebles_por_region.py  
  
# Screenshots  
<div align="center">  

Indice  
![Indice](screenshots/index.png)  
Registro  
![registro](screenshots/registro.png)  
Login y boton de login  
![login](screenshots/login.png)  
Bienvenido  
![bienvenido](screenshots/bienvenido.png)  
Actualizar datos y tipo de usuario   
![actualizar_datos](screenshots/actualizar_datos.png)  
Publicar un inmueble  
![publicar_inmueble](screenshots/publicar_inmueble.png)  
Mis inmuebles  
![mis_inmuebles](screenshots/mis_inmuebles.png)  
Buscar inmuebles  
![buscar_inmuebles](screenshots/buscar_inmuebles.png)  
Inmuebles disponibles  
![inmuebles_disponibles](screenshots/inmuebles_disponibles.png)   
</div>  


