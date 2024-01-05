# myapp/forms.py
from django import forms
from . import models

class PaysForm(forms.ModelForm):
    class Meta:
        model = models.Pays
        fields = ['nom_pays']
