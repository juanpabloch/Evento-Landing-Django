from django import forms
from evento.models import Registro
from django.contrib.auth.models import User


def numbers_letters_validator(word):
    word = word.replace(" ", "")
    for letter in word:
        if letter.isdigit() or not letter.lower().isalpha():
            return False
    return True


class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['nombre', 'apellido', 'email', 'pais', 'telefono', 'puesto_trabajo']
        labels = {
            'email': 'Correo electrónico del trabajo',
            'pais': 'País',
            'telefono': 'Número de teléfono',
            'puesto_trabajo': 'Puesto de trabajo'
        }
        widgets = {
            'telefono': forms.TextInput(attrs={'placeholder': '+541100000000'})
        }

    def clean(self):
        all_clean_data = super().clean()
        nombre = all_clean_data['nombre']
        apellido = all_clean_data['apellido']
        puesto_trabajo = all_clean_data['puesto_trabajo']

        if len(nombre) < 3:
            raise forms.ValidationError({"nombre": ['debe tener mas de 3 letras']})
        if not numbers_letters_validator(nombre):
            raise forms.ValidationError({"nombre": ['no se permiten números ni símbolos']})
        if len(apellido) < 3:
            raise forms.ValidationError({'apellido': ['debe tener mas de 3 letras']})
        if not numbers_letters_validator(apellido):
            raise forms.ValidationError({"apellido": ['no se permiten números ni símbolos']})
        if len(puesto_trabajo) < 3:
            raise forms.ValidationError({'puesto_trabajo': ['debe tener mas de 3 letras']})
        if not numbers_letters_validator(puesto_trabajo):
            raise forms.ValidationError({"puesto_trabajo": ['no se permiten números ni símbolos']})


class UserRegistro(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        help_texts = {
            'username': None
        }
