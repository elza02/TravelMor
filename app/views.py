from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,request
from . import models
from datetime import datetime
from decimal import Decimal
from django.utils import timezone

def home (request):
    # pays1 = models.Pays.objects.create(nom_pays="France")
    # pays2 = models.Pays.objects.create(nom_pays="Spain")
    # pays3 = models.Pays.objects.create(nom_pays="Italy")

    # # Create Ville instances
    # ville1 = models.Ville.objects.create(nom_ville="Paris", id_pays=pays1)
    # ville2 = models.Ville.objects.create(nom_ville="Barcelona", id_pays=pays2)
    # ville3 = models.Ville.objects.create(nom_ville="Rome", id_pays=pays3)

    # # Create Hotel instances
    # hotel1 = models.Hotel.objects.create(
    #     prix_nuit=150.0,
    #     type_hotel = 5,
    #     type_chambre="Standard",
    #     n_chambreDispo=50,
    #     nom_hotel="Eiffel Tower Hotel",
    #     id_ville=ville1,
    # )
    # hotel2 = models.Hotel.objects.create(
    #     prix_nuit=120.0,
    #     type_hotel = 3,
    #     type_chambre="Deluxe",
    #     n_chambreDispo=30,
    #     nom_hotel="Sagrada Familia Hotel",
    #     id_ville=ville2,
    # )
    # hotel3 = models.Hotel.objects.create(
    #     prix_nuit=180.0,
    #     type_hotel = 4,
    #     type_chambre="Suite",
    #     n_chambreDispo=20,
    #     nom_hotel="Colosseum Hotel",
    #     id_ville=ville3,
    # )

    # # Create Image instances
    # image1 = models.Image.objects.create(path_image=".//img.jpeg")
    # #image2 = models.Image.objects.create(path_image="barcelona_image.jpg")
    # #image3 = models.Image.objects.create(path_image="rome_image.jpg")

    # # Create ImageVille instances
    # image_ville1 = models.ImageVille.objects.create(id_images=image1, id_ville=ville1)
    # image_ville2 = models.ImageVille.objects.create(id_images=image1, id_ville=ville2)
    # image_ville3 = models.ImageVille.objects.create(id_images=image1, id_ville=ville3)
    # image_ville1.save()
    # image_ville2.save()
    # image_ville3.save()
    # # Create ImageHotel instances
    # image_hotel1 = models.ImageHotel.objects.create(id_images=image1, id_hotel=hotel1)
    # image_hotel2 = models.ImageHotel.objects.create(id_images=image1, id_hotel=hotel2)
    # image_hotel3 = models.ImageHotel.objects.create(id_images=image1, id_hotel=hotel3)
    # image_hotel1.save()
    # image_hotel2.save()
    # image_hotel3.save()
    # # Create Vol instances
    # vol1 = models.Vol.objects.create(id_vol="FR123", date_d_vol=timezone.now(), date_f_vol=timezone.now(), prix_vol=500.0)
    # vol2 = models.Vol.objects.create(id_vol="ES456", date_d_vol=timezone.now(), date_f_vol=timezone.now(), prix_vol=600.0)
    # vol3 = models.Vol.objects.create(id_vol="IT789", date_d_vol=timezone.now(), date_f_vol=timezone.now(), prix_vol=700.0)

    # # Create Utilisateur instances
    # utilisateur1 = models.Utilisateur.objects.create(
    #     mot_d_passe="pord123",
    #     est_admin=True,
    #     nom="John",
    #     prenom="Doe",
    #     num_telephone="123456789",
    #     email="john@example.com",
    #     path_img_profile="john_profile.jpg",
    #     id_hotel=hotel1,
    # )
    # utilisateur2 = models.Utilisateur.objects.create(
    #     mot_d_passe="pass4",
    #     est_admin=False,
    #     nom="Alice",
    #     prenom="Smith",
    #     num_telephone="987654321",
    #     email="alice@example.com",
    #     path_img_profile="alice_profile.jpg",
    #     id_hotel=hotel2,
    # )
    # utilisateur3 = models.Utilisateur.objects.create(
    #     mot_d_passe="user",
    #     est_admin=False,
    #     nom="Bob",
    #     prenom="Johnson",
    #     num_telephone="555555555",
    #     email="bob@example.com",
    #     path_img_profile="bob_profile.jpg",
    #     id_hotel=hotel3,
    # )

    # # Create Promotion instances
    # promotion1 = models.Promotion.objects.create(
    #     date_d_promo=timezone.now(),
    #     date_f_promo=timezone.now(),
    #     heure_d_promos=timezone.now().time(),
    #     heure_f_promos=timezone.now().time(),
    #     pourcentage=Decimal("10.00"),
    # )
    # promotion2 = models.Promotion.objects.create(
    #     date_d_promo=timezone.now(),
    #     date_f_promo=timezone.now(),
    #     heure_d_promos=timezone.now().time(),
    #     heure_f_promos=timezone.now().time(),
    #     pourcentage=Decimal("15.00"),
    # )
    # promotion3 = models.Promotion.objects.create(
    #     date_d_promo=timezone.now(),
    #     date_f_promo=timezone.now(),
    #     heure_d_promos=timezone.now().time(),
    #     heure_f_promos=timezone.now().time(),
    #     pourcentage=Decimal("20.00"),
    # )

    # # Create Categorie instances
    # categorie1 = models.Categorie.objects.create(nom_categorie="Adventure")
    # categorie2 = models.Categorie.objects.create(nom_categorie="City Break")
    # categorie3 = models.Categorie.objects.create(nom_categorie="Beach Holiday")

    # # Create Voyage instances
    # voyage1 = models.Voyage.objects.create(
    #     titre_voyage = "titre voyage",prix_voyage=1000.0, duree_voyage=5, transport=True, id_hotel=hotel1, id_promotion=promotion1, id_categorie=categorie1
    # )
    # voyage2 = models.Voyage.objects.create(
    #     titre_voyage = "titre voyage",prix_voyage=1200.0, duree_voyage=7, transport=True, id_hotel=hotel2, id_promotion=promotion2, id_categorie=categorie2
    # )
    # voyage3 = models.Voyage.objects.create(
    #     titre_voyage = "titre voyage",prix_voyage=800.0, duree_voyage=4, transport=False, id_hotel=hotel3, id_promotion=promotion3, id_categorie=categorie3
    # )
    # voyage4 = models.Voyage.objects.create(
    #     titre_voyage = "titre voyage 4",prix_voyage=10000.0, duree_voyage=12, transport=False, id_hotel=hotel3, id_categorie=categorie3
    # )
    # voyage4.save()
    # # Create Commentaire instances
    # commentaire1 = models.Commentaire.objects.create(
    #     text_comment="Great experience!", date_redaction=timezone.now().date(), heure_redaction=timezone.now().time(), evaluation=5, id_voyage=voyage1
    # )
    # commentaire2 = models.Commentaire.objects.create(
    #     text_comment="Wonderful trip!", date_redaction=timezone.now().date(), heure_redaction=timezone.now().time(), evaluation=4, id_voyage=voyage2
    # )
    # commentaire3 = models.Commentaire.objects.create(
    #     text_comment="Not bad!", date_redaction=timezone.now().date(), heure_redaction=timezone.now().time(), evaluation=3, id_voyage=voyage3
    # )
    # commentaire1.save()
    # commentaire2.save()
    # commentaire3.save()
    # # Create Notification instances
    # notification1 = models.Notification.objects.create(
    #     date_notif=timezone.now().date(), type="Information", heure_d_notif=timezone.now().time()
    # )
    # notification2 = models.Notification.objects.create(
    #     date_notif=timezone.now().date(), type="Alert", heure_d_notif=timezone.now().time()
    # )
    # notification3 = models.Notification.objects.create(
    #     date_notif=timezone.now().date(), type="Reminder", heure_d_notif=timezone.now().time()
    # )

    # # Create Recevoir instances
    # recevoir1 = models.Recevoir.objects.create(id_utilisateur_1=utilisateur1, id_notification=notification1)
    # recevoir2 = models.Recevoir.objects.create(id_utilisateur_1=utilisateur2, id_notification=notification2)
    # recevoir3 = models.Recevoir.objects.create(id_utilisateur_1=utilisateur3, id_notification=notification3)
    # recevoir1.save()
    # recevoir2.save()
    # recevoir3.save()
    # # Create ReserverVoyage instances
    # reserver_voyage1 = models.ReserverVoyage.objects.create(id_utilisateur_1=utilisateur1, id_voyage=voyage1)
    # reserver_voyage2 = models.ReserverVoyage.objects.create(id_utilisateur_1=utilisateur2, id_voyage=voyage2)
    # reserver_voyage3 = models.ReserverVoyage.objects.create(id_utilisateur_1=utilisateur3, id_voyage=voyage3)
    # reserver_voyage1.save()
    # reserver_voyage2.save()
    # reserver_voyage3.save()
    # # Create Avoir instances
    # avoir1 = models.Avoir.objects.create(id_voyage=voyage1, id_ville=ville1)
    # avoir2 = models.Avoir.objects.create(id_voyage=voyage2, id_ville=ville2)
    # avoir3 = models.Avoir.objects.create(id_voyage=voyage3, id_ville=ville3)
    # avoir1.save()
    # avoir2.save()
    # avoir3.save()
    # # Create Aimer instances
    # aimer1 = models.Aimer.objects.create(id_utilisateur_1=utilisateur1, id_voyage=voyage1)
    # aimer2 = models.Aimer.objects.create(id_utilisateur_1=utilisateur2, id_voyage=voyage2)
    # aimer3 = models.Aimer.objects.create(id_utilisateur_1=utilisateur3, id_voyage=voyage3)
    # aimer1.save()
    # aimer2.save()
    # aimer3.save()
    # # Create inclure instances
    # inclure1 = models.inclure.objects.create(id_voyage=voyage1, id_vol=vol1)
    # inclure2 = models.inclure.objects.create(id_voyage=voyage2, id_vol=vol2)
    # inclure3 = models.inclure.objects.create(id_voyage=voyage3, id_vol=vol3)
    # inclure1.save()
    # inclure2.save()
    # inclure3.save()
    return render(request, 'home.html', {})



def voyage_organise(request):
    # av = Avoir.objects.all()
    # img = ImageHotel.objects
    # return render(request, 'voyage_organise.html', {'query' : av,'img' : img})
    # query = models.Avoir.objects.select_related('id_voyage__id__hotel', 'id_voyage__id__promotion', 'id_voyage__id__categorie', 'id_ville__id__pays')
    query = models.Avoir.objects.select_related(
        'id_voyage__id_hotel__id_ville__id_pays',
        'id_voyage__id_promotion',
        'id_voyage__id_categorie',
        'id_ville__id_pays'
    ).filter(id_voyage__id_promotion__isnull=True)
    print(str(query.query))
    query = query.all()
    return render(request, 'voyage_organise.html', {'query' : query})



def voyage_organise_details(request, id_voyage):
    # av = Avoir.objects.all()
    # img = ImageHotel.objects
    # return render(request, 'voyage_organise.html', {'query' : av,'img' : img})
    # query = models.Avoir.objects.select_related('id_voyage__id__hotel', 'id_voyage__id__promotion', 'id_voyage__id__categorie', 'id_ville__id__pays')
    avoir_instance = get_object_or_404(models.Avoir.objects.select_related(
            'id_voyage__id_hotel',
            'id_voyage__id_promotion',
            'id_voyage__id_categorie',
            'id_ville__id_pays'
        ), id=id_voyage)
    return render(request, 'voyage_organise_details.html', {'avoir_instance' : avoir_instance})



def paysRelatedToVoyage(ville):
    return models.Avoir.objects.get(id_ville = ville).id_ville.id_pays



def promotions(request):
    query = models.Avoir.objects.select_related(
        'id_voyage__id_hotel__id_ville__id_pays',  # Inclure le pays lié à l'hôtel
        'id_voyage__id_promotion',
        'id_voyage__id_categorie',
        'id_ville__id_pays'  # Inclure le pays lié à la ville
        ).all()
    return render(request, 'promotions.html', {'query' : query})



def promotions_details(request, id_voyage):
    # av = Avoir.objects.all()
    # img = ImageHotel.objects
    # return render(request, 'promotions.html', {'query' : av,'img' : img})
    # query = models.Avoir.objects.select_related('id_voyage__id__hotel', 'id_voyage__id__promotion', 'id_voyage__id__categorie', 'id_ville__id__pays')
    # First, check if the promotion with pourcentage greater than 0 exists
    promotion = get_object_or_404(models.Promotion, pourcentage__gt=0)
    # Then, fetch the Avoir instances related to the promotion
    avoir_instance = models.Avoir.objects.select_related(
        'id_voyage__id_hotel',
        'id_voyage__id_promotion',
        'id_voyage__id_categorie',
        'id_ville__id_pays'
    ).filter(id_promotion=promotion)
    return render(request, 'promotions_details.html', {'avoir_instance' : avoir_instance})

def hotels(request):
    return render(request, 'hotels.html', {})

def hotels_details(request):
    return render(request, 'hotels_details.html', {})


def special_turqie(request):
    return render(request, 'special_turqie.html', {})

def special_turqie_details(request):
    return render(request, 'special_turqie_details.html', {})

def special_asie(request):
    return render(request, 'special_asie.html', {})

def special_asie_details(request):
    return render(request, 'special_asie_details.html', {})

def special_omra(request):
    return render(request, 'special_omra.html', {})

def special_omra_details(request):
    return render(request, 'special_omra_details.html', {})

def special_haj(request):
    return render(request, 'special_haj.html', {})

def special_haj_details(request):
    return render(request, 'special_haj_details.html', {})
