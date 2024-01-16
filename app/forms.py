# myapp/forms.py
from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

    
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

class VoyageModificationForm(forms.ModelForm):
    class Meta:
        model = models.Voyage
        fields = ['id_voyage', 'titre_voyage', 'prix_voyage', 'duree_voyage', 'transport', 'id_hotel', 'id_promotion', 'id_categorie']
        labels = {
            'id_voyage': 'Voyage ID',
            'titre_voyage': 'Titre Voyage',
            'prix_voyage': 'Prix Voyage',
            'duree_voyage': 'Durée Voyage',
            'transport': 'Transport',
        }
    # Utiliser ModelChoiceField avec les noms affichés
    id_hotel = forms.ModelChoiceField(queryset=models.Hotel.objects.all(), empty_label=None, to_field_name='nom_hotel')
    id_promotion = forms.ModelChoiceField(queryset=models.Promotion.objects.all(), required=False, empty_label=None, to_field_name='pourcentage')
    id_categorie = forms.ModelChoiceField(queryset=models.Categorie.objects.all(), empty_label=None, to_field_name='nom_categorie')
class VoyageAjoutForm(forms.ModelForm):
    class Meta:
        model = models.Voyage
        fields = ['titre_voyage', 'prix_voyage', 'duree_voyage', 'transport', 'id_hotel', 'id_promotion', 'id_categorie']
        labels = {
            'titre_voyage': 'Titre Voyage',
            'prix_voyage': 'Prix Voyage',
            'duree_voyage': 'Durée Voyage',
            'transport': 'Transport',
        }
    # Utiliser ModelChoiceField avec les noms affichés
    id_hotel = forms.ModelChoiceField(queryset=models.Hotel.objects.all(), empty_label=None, to_field_name='nom_hotel')
    id_promotion = forms.ModelChoiceField(queryset=models.Promotion.objects.all(), required=False, empty_label=None, to_field_name='pourcentage')
    id_categorie = forms.ModelChoiceField(queryset=models.Categorie.objects.all(), empty_label=None, to_field_name='nom_categorie')

class HotelModificationForm(forms.ModelForm):
    class Meta:
        model = models.Hotel
        fields = ['id_hotel','nom_hotel', 'prix_nuit', 'type_chambre', 'type_hotel', 'n_chambreDispo', 'petit_dejeuner','id_ville']

    # Utiliser ModelChoiceField avec les noms affichés
    id_ville = forms.ModelChoiceField(queryset=models.Ville.objects.all(), empty_label=None, to_field_name='nom_ville')
class HotelAjoutForm(forms.ModelForm):
    class Meta:
        model = models.Hotel
        fields = ['nom_hotel', 'prix_nuit', 'type_chambre', 'type_hotel', 'n_chambreDispo', 'petit_dejeuner','id_ville']

    # Utiliser ModelChoiceField avec les noms affichés
    id_ville = forms.ModelChoiceField(queryset=models.Ville.objects.all(), empty_label=None, to_field_name='nom_ville')

class PromotionModificationForm(forms.ModelForm):
    class Meta:
        model = models.Promotion
        fields = ['id_promotion','date_d_promo', 'date_f_promo', 'heure_d_promos', 'heure_f_promos', 'pourcentage']
        labels = {
            'id_promotion': 'Promotion ID',
            'date_d_promo': 'Date debut promotion',
            'date_f_promo': 'Date Fin promotion',
            'heure_d_promos': 'Heure Debut promotion',
            'heure_f_promos': 'Heure Fin promotion',
            'pourcentage': 'Valeur promotion',
        }
        widgets = {
            'date_d_promo': forms.DateInput(attrs={'type': 'date'}),
            'date_f_promo': forms.DateInput(attrs={'type': 'date'}),
            'heure_d_promos': forms.TimeInput(attrs={'type': 'time'}),
            'heure_f_promos': forms.TimeInput(attrs={'type': 'time'}),
        }
class PromotionAjoutForm(forms.ModelForm):
    class Meta:
        model = models.Promotion
        fields = ['date_d_promo', 'date_f_promo', 'heure_d_promos', 'heure_f_promos', 'pourcentage']
        labels = {
            'date_d_promo': 'Date debut promotion',
            'date_f_promo': 'Date Fin promotion',
            'heure_d_promos': 'Heure Debut promotion',
            'heure_f_promos': 'Heure Fin promotion',
            'pourcentage': 'Valeur promotion',
        }
        widgets = {
            'date_d_promo': forms.DateInput(attrs={'type': 'date'}),
            'date_f_promo': forms.DateInput(attrs={'type': 'date'}),
            'heure_d_promos': forms.TimeInput(attrs={'type': 'time'}),
            'heure_f_promos': forms.TimeInput(attrs={'type': 'time'}),
        }

class VolModificationForm(forms.ModelForm):
    class Meta:
        model = models.Vol
        fields = ['id_vol','date_d_vol', 'date_f_vol', 'prix_vol']
        labels = {
            'id_vol': 'Vol ID',
            'date_d_vol': 'Date debut vol',
            'date_f_vol': 'Date Fin vol',
            'prix_vol': 'Prix du vol',
        }
        widgets = {
            'date_d_vol': forms.DateInput(attrs={'type': 'date'}),
            'date_f_vol': forms.DateInput(attrs={'type': 'date'}),
        }
class VolAjoutForm(forms.ModelForm):
    class Meta:
        model = models.Vol
        fields = ['id_vol','date_d_vol', 'date_f_vol', 'prix_vol']
        labels = {
            'id_vol': 'Vol ID',
            'date_d_vol': 'Date debut vol',
            'date_f_vol': 'Date Fin vol',
            'prix_vol': 'Prix du vol',
        }
        widgets = {
            'date_d_vol': forms.DateInput(attrs={'type': 'date'}),
            'date_f_vol': forms.DateInput(attrs={'type': 'date'}),
        }

class VilleModificationForm(forms.ModelForm):
    class Meta:
        model = models.Ville
        fields = ['id_ville','nom_ville', 'id_pays']
        # labels = {
        #     'id_ville': 'Ville ID',
        #     'nom_ville': 'Nom Ville',
        #     'id_pays': 'Nom Pays',
        # }
    id_pays = forms.ModelChoiceField(queryset=models.Pays.objects.all(), empty_label=None, to_field_name='nom_pays')

class VilleAjoutForm(forms.ModelForm):
    class Meta:
        model = models.Ville
        fields = ['nom_ville', 'id_pays']
        labels = {
            'nom_ville': 'Nom Ville',
            'id_pays': 'Nom Pays',
        }
    id_pays = forms.ModelChoiceField(queryset=models.Pays.objects.all(), empty_label=None, to_field_name='nom_pays')

class PaysModificationForm(forms.ModelForm):
    class Meta:
        model = models.Pays
        fields = ['id_pays','nom_pays']
        labels = {
            'id_pays': 'Pays ID',
            'nom_pays': 'Nom Pays',
        }

class PaysAjoutForm(forms.ModelForm):
    class Meta:
        model = models.Pays
        fields = ['nom_pays']
        labels = {
            'nom_pays': 'Nom Pays',
        }