from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(error_messages={'invalid': 'Ingresa un email valido'})

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		error_messages = {
            'username': {
                'max_length': 'El nombre de usuario es muy largo.',
            },
            'password1': {
                'min_length': 'La contraseña es muy corta.',
                'invalid' : 'No es una contraseña valida',
                'password_mismatch' : 'No es la misma contraseña',
            },
            'password2': {
                'min_length': "La contraseña es muy corta.",
                'invalid' : "No es una contraseña valida",
                'password_mismatch' : "No es la misma contraseña",
            },
        }

class UserUpdatedForm(forms.ModelForm):
	email = forms.EmailField(error_messages={'invalid': 'Ingresa un email valido'})

	class Meta:
		model = User
		fields = ['username', 'email']



