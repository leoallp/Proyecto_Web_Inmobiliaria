
#models.py
from django.db import models    
from django.contrib.auth.models import User 

class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self) -> str:
        return  f"{self.nombre} - {self.descripcion}"
    
class Usuario(models.Model):
    
    user = models.OneToOneField(User, on_delete= models.CASCADE, null=False) #de User ya heredan nombre, password y correo
    tipo_usuario = models.ForeignKey(TipoUsuario,null= True, on_delete= models.CASCADE )#FK uno a muchos
    rut = models.CharField(max_length=10,null=False, unique=True)
    direccion = models.CharField(max_length=255, null=False, blank=False)  
    telefono = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.user.first_name} - {self.user.last_name} "
    
    
    
class Pais(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.nombre
    
class Region(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    pais = models.ForeignKey(Pais, null=True, blank=True, on_delete=models.CASCADE)#FK uno a muchos
    def __str__(self):
        return self.nombre
    
class Comuna(models.Model):
    nombre= models.CharField(max_length=100, null=False, blank=False)
    region = models.ForeignKey(Region,null= False, blank= False, on_delete= models.CASCADE )#FK uno a muchos
    def __str__(self):
        return f"{self.nombre} - Region: {self.region.nombre}"
    
    
class TipoInmueble(models.Model):       #pueden ser inmuebles como estacionamiento, parcela, departamento y casa
    nombre = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return self.nombre
    
class Inmueble(models.Model):
    
    disponibilidad = models.BooleanField(default=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.TextField()
    m2_construidos = models.FloatField(null=False)
    m2_totales_o_del_terreno = models.FloatField(null=False)
    numero_de_estacionamientos = models.IntegerField(default=0)
    numero_de_habitaciones = models.IntegerField(default=0)
    numero_de_banios = models.IntegerField(default=0)
    precio_mensual = models.FloatField(null=False)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    region = models.ForeignKey(Region, null=False, blank=False, on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, null=False, blank=False, on_delete=models.CASCADE)
    tipo_inmueble = models.ForeignKey(TipoInmueble, null=False, blank=False, on_delete=models.CASCADE)
    usuarios =models.ManyToManyField(Usuario, related_name='inmuebles')
    
    def __str__(self) -> str:
        return f"{self.nombre}-{self.tipo_inmueble}-{self.usuarios}"