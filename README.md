# <div align="center" > "INMOBILIARIA LL" </div>


<div align="center" > APLICACION WEB DE BUSQUEDA, PUBLICACION Y ARRIENDO DE INMUEBLES   </div> <br><br>   

![Indice](screenshots/0.png)  

# ******** Algunas sugerencias de instalación ********

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
  
# Algunos Screenshots  
<div align="center">  

Indice  
![Indice](screenshots/1.png) <br><br>     
Registro  
![registro](screenshots/2.png) <br><br>     
Buscar inmuebles  
![buscar_inmuebles](screenshots/3.png)  <br><br>    
Inmuebles disponibles  
![inmuebles_disponibles](screenshots/4.png)  <br><br>   
Publicar un inmueble  
![publicar_inmueble](screenshots/5.png)  <br><br>    
Mis inmuebles  
![mis_inmuebles](screenshots/6.png)  

</div>  


