from django import forms
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User   


class CreateUserForm(UserCreationForm):
    phone_number = forms.CharField(max_length=12)
    class Meta:
        model = User
        fields = ['username','first_name','email','phone_number','password1','password2']

        widgets = {'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de usuario'}),
                  'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
                  'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
                  'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':'phone_number'}),
                  'password1':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contreaseña'}),
                  'password2':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Confirma contraseña'}),
                  }
        