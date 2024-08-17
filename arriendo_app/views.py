#views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth import login
from .forms import *
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Funciones para verificar el tipo de usuario
def es_arrendador(user):
    return user.usuario.tipo_usuario.nombre == 'Arrendador'

def es_arrendatario(user):
    return user.usuario.tipo_usuario.nombre == 'Arrendatario'

# vista formulario inicio de sesion
def inicio_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso. ¡Bienvenido!')
            return redirect('bienvenido')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

#vista para editar los inmuebles del arrendador
@login_required
@user_passes_test(es_arrendador)  #comprueba que el tipo de usuario sea arrendador
def editar_inmueble(request, inmueble_id):
    nombre_usuario = request.user.get_username()
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)

    if request.method == 'POST':
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save() # Guarda los datos del formulario
            messages.success(request, 'Inmueble actualizado correctamente.')
            return redirect('mis_inmuebles')  
    else:
        form = InmuebleForm(instance=inmueble)

    return render(request, 'editar_inmueble.html', {'form': form,  "nombre_usuario": nombre_usuario})

def user_data_complete(user):
    try:
        usuario = user.usuario
        return bool(usuario.rut and usuario.direccion and usuario.telefono and usuario.tipo_usuario)
    except Usuario.DoesNotExist:
        return False

#obliga al usuario a completar todo el formulario de registro
def user_data_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if not user_data_complete(request.user):
            messages.info(request, 'Por favor, complete sus datos antes de continuar.')
            return redirect('actualizar_datos')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

#vista arrendatario con selector multiple de busqueda
@login_required
@user_passes_test(es_arrendatario)
def buscar_propiedad(request):
    nombre_usuario = request.user.get_username()
    tipos_inmuebles = TipoInmueble.objects.all()
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    return render(request, 'buscar_propiedad.html', {'tipos_inmuebles': tipos_inmuebles, 'regiones': regiones, 'comunas': comunas,  'nombre_usuario': nombre_usuario})

#vista arrendatario inmubles disponibles tras la busqueda
@login_required
@user_passes_test(es_arrendatario)
def inmuebles_disponibles(request):
    nombre_usuario = request.user.get_username()
    if request.method == 'POST':
        tipo_inmueble = request.POST.get('tipo_inmueble')
        region = request.POST.get('regiones')
        comuna = request.POST.get('comunas')

        inmuebles = Inmueble.objects.filter(disponibilidad=True)

        if tipo_inmueble:
            inmuebles = inmuebles.filter(tipo_inmueble_id=tipo_inmueble)
        if region:
            inmuebles = inmuebles.filter(region_id=region)
        if comuna:
            inmuebles = inmuebles.filter(comuna_id=comuna)

        return render(request, 'inmuebles_disponibles.html', {'inmuebles': inmuebles, "nombre_usuario": nombre_usuario})
    else:
        return render(request, 'inmuebles_disponibles.html', {'inmuebles': [], "nombre_usuario": nombre_usuario})

#lista de inmuebles creados
@login_required
@user_passes_test(es_arrendador)
def mis_inmuebles(request):
    nombre_usuario = request.user.get_username()
    usuario = request.user.usuario
    inmuebles = Inmueble.objects.filter(usuarios=usuario)  # Filtra los inmuebles por el usuario actual

    if request.method == 'POST':
        inmueble_id = request.POST.get('inmueble_id')
        inmueble = get_object_or_404(Inmueble, id=inmueble_id)
        
        if 'update' in request.POST:
            form = InmuebleForm(request.POST, instance=inmueble)
            if form.is_valid():
                form.save() # Guarda los datos del formulario
                messages.success(request, 'Inmueble actualizado correctamente')
                return redirect('mis_inmuebles')
        elif 'delete' in request.POST:
            inmueble.delete()
            messages.success(request, 'Inmueble eliminado correctamente')
            return redirect('mis_inmuebles')
    else:
        form = InmuebleForm()

    return render(request, 'mis_inmuebles.html', {'inmuebles': inmuebles, 'form': form, "nombre_usuario": nombre_usuario})

#formulario para crear inmueble
@login_required
@user_passes_test(es_arrendador)
def crear_inmueble(request):
    nombre_usuario = request.user.get_username()
    
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.save()
            inmueble.usuarios.add(request.user.usuario)  # Asocia el inmueble con el usuario actual
            messages.success(request, 'Inmueble agregado correctamente.')
            return redirect('mis_inmuebles')
    else:
        form = InmuebleForm()
    return render(request, 'crear_inmueble.html', {'form': form, "nombre_usuario": nombre_usuario})

#select multiple usado en vista buscar_propiedades
def filtrar_comunas(request):
    try:
        if request.method == "POST":
            print("** request.body **", request.body)
            data = json.loads(request.body)
            regionId = data.get('regionId')
            print('** region id **', regionId)

            if not regionId:
                return JsonResponse({'error': 'regionId es requerido'}, status=400)

            dataBD = list(Comuna.objects.filter(region=regionId).values())
            print('** dataBD **', dataBD)
            return JsonResponse({'status': 200, 'data': dataBD})
        else:
            return JsonResponse({'error': 'Método no permitido'}, status=405)
    except Exception as e:
        print("** Exception **", str(e))
        return JsonResponse({'error': str(e)}, status=400)
    
#bienvenido    
@login_required
def bienvenido(request):
    titulo_pag = "Bienvenido"
    
    nombre_usuario = request.user.get_username()
    context = {
        "nombre_usuario": nombre_usuario,
        'titulo_pag': titulo_pag,
    }
    
    return render(request,'bienvenido.html', context)            
    

#formulario para actualizar datos
@login_required
def actualizar_datos(request):
    nombre_usuario = request.user.get_username()  
    usuario, created = Usuario.objects.get_or_create(user=request.user)  # Obtiene o crea un objeto Usuario asociado al usuario actual
    if request.method == 'POST':
        # Si el método de la solicitud es POST, se procesan los datos del formulario
        form = ActualizarDatosForm(request.POST, instance=usuario, user=request.user)  # Crea una instancia del formulario con los datos POST y el usuario
        if form.is_valid():
            form.save()  
            messages.success(request, 'Datos actualizados correctamente')  
            return redirect('bienvenido') 
    else:
        # Si el método de la solicitud no es POST, se crea un formulario vacío
        form = ActualizarDatosForm(instance=usuario, user=request.user)  # Crea una instancia del formulario con el objeto Usuario
    context = {
        "nombre_usuario": nombre_usuario,  
        'form': form,  
        'tipousuario': TipoUsuario.objects.all()  # Pasa todos los objetos TipoUsuario al contexto
    }
    return render(request, 'actualizar_datos.html', context)  

#home
def index(request):
    nombre_usuario = request.user.get_username()
    context = {
        "nombre_usuario": nombre_usuario,
    }
    return render(request,"index.html", context)

#formulario de registro
def registro(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso. Bienvenido!')
            return redirect('bienvenido')
        else:
            print("Errores de formulario:", form.errors)
            # Agregar mensajes de error
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = RegisterForm()
    
    return render(request, 'registro.html', {'form': form})

