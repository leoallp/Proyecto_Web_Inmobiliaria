from .models import Comuna, Region, TipoInmueble, Usuario, Inmueble, Direccion 

# a. Crear un objeto con el modelo
def crear_inmueble(pdisponibilidad, pnombre, pdescripcion,pm2_construidos,pm2_totales_o_del_terreno,pnumero_de_estacionamientos,pnumero_de_habitaciones,pnumero_de_banios,pprecio_mensual): #data puede ser un qeriset, json, lista
    pcomuna = Comuna.objects.get(pk=95)
    pregion = Region.objects.get(pk=12)
    pdireccion = Direccion.objects.get(pk=1)
    ptipo_inmueble = TipoInmueble.objects.get(pk=4)
    inmueble = Inmueble(
        disponibilidad=pdisponibilidad,  # Ejemplo de datos, ajustar según necesidad
        nombre=pnombre,
        descripcion=pdescripcion,
        m2_construidos=pm2_construidos,
        m2_totales_o_del_terreno=pm2_totales_o_del_terreno,
        numero_de_estacionamientos=pnumero_de_estacionamientos,
        numero_de_habitaciones=pnumero_de_habitaciones,
        numero_de_banios=pnumero_de_banios,
        precio_mensual=pprecio_mensual,
        direccion=pdireccion,
        comuna=pcomuna,
        region=pregion,
        tipo_inmueble=ptipo_inmueble,
        
    )
    
    inmueble.save() 
    
def asignar_arrendatario_inmueble(arrendatario_id, inmueble_id):
    inmueble = Inmueble.objects.get(pk=inmueble_id)
    arrendatario = Usuario.objects.get(pk= arrendatario_id)
    inmueble.usuarios.add(arrendatario)

#b. Enlistar desde el modelo de datos.
def mostrar_inmuebles():
    lista_inmuebles = Inmueble.objects.all()
    return lista_inmuebles
#c. Actualizar un registro en el modelo de datos.

#d. Borrar un registro del modelo de datos utilizando un modelo Django.

def eliminar_inmueble(inmueble_id):
    Inmueble.objects.get(pk=inmueble_id).delete()