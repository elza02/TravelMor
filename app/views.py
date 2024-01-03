from django.shortcuts import render
from django.http import HttpResponse,request
from . import models
def home (request):
    # Création d'instances pour le modèle Notification
notification1 = Notification.objects.create(date_notif='2023-01-01', type='Info', heure_d_notif='12:00:00')
notification2 = Notification.objects.create(date_notif='2023-01-02', type='Promo', heure_d_notif='15:30:00')

# Création d'instances pour le modèle Promotion
promotion1 = Promotion.objects.create(date_d_promo='2023-02-01', date_f_promo='2023-02-15', heure_d_promos='08:00:00', heure_f_promos='18:00:00', pourcentage=10.00)
promotion2 = Promotion.objects.create(date_d_promo='2023-03-01', date_f_promo='2023-03-15', heure_d_promos='09:30:00', heure_f_promos='17:00:00', pourcentage=15.50)

# Création d'instances pour le modèle Categorie
categorie1 = Categorie.objects.create(nom_categorie='Aventure')
categorie2 = Categorie.objects.create(nom_categorie='Plage')

# Création d'instances pour le modèle Pays
pays1 = Pays.objects.create(nom_pays='France')
pays2 = Pays.objects.create(nom_pays='Espagne')

# Création d'instances pour le modèle Ville
ville1 = Ville.objects.create(nom_ville='Paris', id_pays=pays1)
ville2 = Ville.objects.create(nom_ville='Barcelone', id_pays=pays2)

# Création d'instances pour le modèle Hotel
hotel1 = Hotel.objects.create(prix_nuit=150.00, type_chambre='Double', n_chambreDispo=20, nom_hotel='Le Grand', id_ville=ville1)
hotel2 = Hotel.objects.create(prix_nuit=120.00, type_chambre='Simple', n_chambreDispo=15, nom_hotel='Plaza', id_ville=ville2)

# Création d'instances pour le modèle Image
image1 = Image.objects.create(path_image='path_image_1.jpg')
image2 = Image.objects.create(path_image='path_image_2.jpg')

# Création d'instances pour le modèle ImageVille
image_ville1 = ImageVille.objects.create(id_images=image1, id_ville=ville1)
image_ville2 = ImageVille.objects.create(id_images=image2, id_ville=ville2)

# Création d'instances pour le modèle ImageHotel
image_hotel1 = ImageHotel.objects.create(id_images=image1, id_hotel=hotel1)
image_hotel2 = ImageHotel.objects.create(id_images=image2, id_hotel=hotel2)

# Continuer de la même manière pour les autres modèles...



    