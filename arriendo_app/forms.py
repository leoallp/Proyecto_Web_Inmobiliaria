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
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    password = forms.CharField(required=False, widget=forms.PasswordInput, help_text="Déjalo en blanco si no quieres cambiarlo.")

    class Meta:
        model = Usuario
        fields = ['rut', 'direccion', 'telefono', 'tipo_usuario']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ActualizarDatosForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['username'].initial = user.username
            self.fields['email'].initial = user.email
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name

    def save(self, commit=True):
        usuario = super(ActualizarDatosForm, self).save(commit=False)
        user = usuario.user
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        password = self.cleaned_data['password']
        if password:
            user.set_password(password)
        if commit:
            user.save()
            usuario.save()
        return usuario

class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = [
            'disponibilidad', 'nombre', 'descripcion', 'm2_construidos', 'm2_totales_o_del_terreno',
            'numero_de_estacionamientos', 'numero_de_habitaciones', 'numero_de_banios', 'precio_mensual',
            'direccion', 'region', 'comuna', 'tipo_inmueble'
        ]
        widgets = {
            'region': forms.Select(attrs={'class': 'form-select', 'id': 'id_region', 'onchange': 'filtrarComunas(this.value)'}),
            'comuna': forms.Select(attrs={'class': 'form-select', 'id': 'id_comuna'}),
        }

