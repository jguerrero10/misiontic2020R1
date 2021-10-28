from django.forms import ModelForm
from django import forms

from loanapp.models import *

class UsuarioForm(forms.Form):
    usuario = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    correo = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'nombre@correo'
    }))
    password = forms.CharField(max_length=12, widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    password_verificar = forms.CharField(max_length=12, widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(max_length=12, widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))







