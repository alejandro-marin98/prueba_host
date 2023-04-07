from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
import re


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label="Nombre de usuario:", max_length=20) 
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    email = forms.EmailField(max_length=50, required=None)
    biografia = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}), max_length=1000, label='Sobre tí',
                                required=False)
    class Meta:
        model = User
        fields = ["username", "password", "email", "biografia"]
        db_table = 'login_user'

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 6:
            raise forms.ValidationError('* El nombre debe de tener una longitud de al menos 6 caracteres.')

        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('* El nombre de usuario ya está en uso.')
        return username
    
    def clean_password(self):
        pw = self.cleaned_data['password']
        
        if len(pw) < 6:
            raise forms.ValidationError('* La contraseña debe de tener una longitud de al menos 6 caracteres.')        
        return pw
    def clean_email(self):
        email_inp = self.cleaned_data.get('email')
        user = None
        try:
            user = User.objects.get(email=email_inp)
        except:
            pass
        
        if (user is not None):
            raise forms.ValidationError('* Correo ya registrado.')             

        return email_inp



class FormularioLogin(forms.Form):
    username = forms.CharField(label='Nombre de usuario:', min_length=5, max_length=150)
    password = forms.CharField(
        label='Contraseña:', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password"]
        db_table = 'login_user'
    
    def clean_username(self):
        return self.cleaned_data.get('username')

    def clean_password(self):
        user = self.cleaned_data.get('username')
        passw = self.cleaned_data.get('password')
        username_taken = User.objects.filter(username=user, password=passw)
        if not username_taken:
            raise forms.ValidationError('* ERROR: Usuario y/o contraseña incorrectos.')
        return passw

