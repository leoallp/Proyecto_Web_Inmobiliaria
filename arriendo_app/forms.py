# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Inmueble, TipoUsuario

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ActualizarDatosForm(forms.ModelForm):
    # Definimos campos adicionales para el formulario
    username = forms.CharField(required=True)  # Campo de nombre de usuario (obligatorio)
    email = forms.EmailField(required=True)    # Campo de correo electrónico (obligatorio)
    first_name = forms.CharField(required=False)  # Campo de nombre (opcional)
    last_name = forms.CharField(required=False)   # Campo de apellido (opcional)
    password = forms.CharField(
        required=False, 
        widget=forms.PasswordInput(attrs={'placeholder': '********'}),  # Campo para la contraseña con entrada oculta  
    )

    class Meta:
        model = Usuario  # Especifica el modelo asociado al formulario
        fields = ['rut', 'direccion', 'telefono', 'tipo_usuario']  # Campos del modelo que se incluyen en el formulario

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Extrae el objeto de usuario de los argumentos
        super().__init__(*args, **kwargs)  # Llama al inicializador de la clase base
        if user:
            # Inicializa los campos del formulario con los valores actuales del usuario
            self.fields['username'].initial = user.username
            self.fields['email'].initial = user.email
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name

    def save(self, commit=True):
        usuario = super().save(commit=False)  # Guarda el modelo sin comprometerlo todavía
        user = usuario.user  # Obtiene el usuario asociado al objeto Usuario
        # Actualiza los atributos del usuario con los datos del formulario
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])  # Actualiza la contraseña si se proporcionó
        if commit:
            user.save()  # Guarda los cambios en el usuario
            usuario.save()  # Guarda los cambios en el objeto Usuario
        return usuario  # Devuelve el objeto Usuario actualizado

class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = [
            'nombre', 'descripcion', 'm2_construidos', 'm2_totales_o_del_terreno',
            'numero_de_estacionamientos', 'numero_de_habitaciones', 'numero_de_banios', 'precio_mensual',
            'direccion', 'region', 'comuna', 'tipo_inmueble', 'disponibilidad'
        ]
        widgets = {
            'region': forms.Select(attrs={'class': 'form-select', 'id': 'id_region', 'onchange': 'filtrarComunas(this.value)'}),
            'comuna': forms.Select(attrs={'class': 'form-select', 'id': 'id_comuna'}),
        }

