# myapp/forms.py
from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

    
class PaysForm(forms.ModelForm):
    class Meta:
        model = models.Pays
        fields = ['nom_pays']


class SimpleForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, label='Mot de passe')


class RegistrationForm(forms.Form):
    nom = forms.CharField()
    prenom = forms.CharField()
    num_telephone = forms.CharField()
    email = forms.EmailField()
    mot_d_passe = forms.CharField(widget=forms.PasswordInput, label='Mot de passe')
    path_img_profile = forms.ImageField()