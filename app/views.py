from decimal import Decimal
from django.forms import model_to_dict
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import *
from .forms import *
from django.urls import reverse
# from app.forms import PaysForm
from . import models
from django.utils import timezone
from django.http import HttpRequest, HttpResponse, JsonResponse
import json
from json import JSONEncoder
from datetime import date, time

def home (request):
    # pays1 = models.Pays.objects.create(nom_pays="France")
    # pays2 = models.Pays.objects.create(nom_pays="Spain")
    # pays3 = models.Pays.objects.create(nom_pays="Italy")
    # pays4 = models.Pays.objects.create(nom_pays="Saudi arabia")
    # pays5 = models.Pays.objects.create(nom_pays="Turquie")
    # pays6 = models.Pays.objects.create(nom_pays="Japan")
    # # Create Ville instances
    # ville1 = models.Ville.objects.create(nom_ville="Paris", id_pays=pays1)
    # ville2 = models.Ville.objects.create(nom_ville="Barcelona", id_pays=pays2)
    # ville3 = models.Ville.objects.create(nom_ville="Rome", id_pays=pays3)
    # ville4 = models.Ville.objects.create(nom_ville="Makkah", id_pays=pays4)
    # ville5 = models.Ville.objects.create(nom_ville="Istanbul", id_pays=pays5)
    # ville6 = models.Ville.objects.create(nom_ville="Tokyo", id_pays=pays6)

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
    # hotel4 = models.Hotel.objects.create(
    #     prix_nuit=180.0,
    #     type_hotel = 4,
    #     type_chambre="Suite",
    #     n_chambreDispo=20,
    #     nom_hotel="AL WAHA",
    #     id_ville=ville4,
    # )
    # hotel5 = models.Hotel.objects.create(
    #     prix_nuit=180.0,
    #     type_hotel = 4,
    #     type_chambre="Suite",
    #     n_chambreDispo=20,
    #     nom_hotel="AL KHAYR",
    #     id_ville=ville5,
    # )
    # hotel6 = models.Hotel.objects.create(
    #     prix_nuit=180.0,
    #     type_hotel = 4,
    #     type_chambre="Standart",
    #     n_chambreDispo=20,
    #     nom_hotel="LA CASA",
    #     id_ville=ville6,
    # )

    # # Create Image instances
    # image1 = models.Image.objects.create(path_image=".//img.jpeg")
    # #image2 = models.Image.objects.create(path_image="barcelona_image.jpg")
    # #image3 = models.Image.objects.create(path_image="rome_image.jpg")

    # # Create ImageVille instances
    # image_ville1 = models.ImageVille.objects.create(id_images=image1, id_ville=ville1)
    # image_ville2 = models.ImageVille.objects.create(id_images=image1, id_ville=ville2)
    # image_ville3 = models.ImageVille.objects.create(id_images=image1, id_ville=ville3)
    # image_ville4 = models.ImageVille.objects.create(id_images=image1, id_ville=ville4)
    # image_ville5 = models.ImageVille.objects.create(id_images=image1, id_ville=ville5)
    # image_ville6 = models.ImageVille.objects.create(id_images=image1, id_ville=ville6)
    # image_ville1.save()
    # image_ville2.save()
    # image_ville3.save()
    # image_ville4.save()
    # image_ville5.save()
    # image_ville6.save()
    # # Create ImageHotel instances
    # image_hotel1 = models.ImageHotel.objects.create(id_images=image1, id_hotel=hotel1)
    # image_hotel2 = models.ImageHotel.objects.create(id_images=image1, id_hotel=hotel2)
    # image_hotel3 = models.ImageHotel.objects.create(id_images=image1, id_hotel=hotel3)
    # image_hotel4 = models.ImageHotel.objects.create(id_images=image1, id_hotel=hotel4)
    # image_hotel5 = models.ImageHotel.objects.create(id_images=image1, id_hotel=hotel5)
    # image_hotel6 = models.ImageHotel.objects.create(id_images=image1, id_hotel=hotel6)
    # image_hotel1.save()
    # image_hotel2.save()
    # image_hotel3.save()
    # image_hotel4.save()
    # image_hotel5.save()
    # image_hotel6.save()
    # # Create Vol instances
    # vol1 = models.Vol.objects.create(id_vol="FR123", date_d_vol=timezone.now(), date_f_vol=timezone.now(), prix_vol=500.0)
    # vol2 = models.Vol.objects.create(id_vol="ES456", date_d_vol=timezone.now(), date_f_vol=timezone.now(), prix_vol=600.0)
    # vol3 = models.Vol.objects.create(id_vol="IT789", date_d_vol=timezone.now(), date_f_vol=timezone.now(), prix_vol=700.0)
    # vol4 = models.Vol.objects.create(id_vol="FFR55", date_d_vol=timezone.now(), date_f_vol=timezone.now(), prix_vol=900.0)
    # vol5 = models.Vol.objects.create(id_vol="E5DD7", date_d_vol=timezone.now(), date_f_vol=timezone.now(), prix_vol=3000.0)
    # vol6 = models.Vol.objects.create(id_vol="XX9OP", date_d_vol=timezone.now(), date_f_vol=timezone.now(), prix_vol=10235.0)

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
    #     pourcentage=Decimal("0.00"),
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
    # categorie1 = models.Categorie.objects.create(nom_categorie="special_asie")
    # categorie2 = models.Categorie.objects.create(nom_categorie="special_turquie")
    # categorie3 = models.Categorie.objects.create(nom_categorie="special_omra")
    # categorie4 = models.Categorie.objects.create(nom_categorie="special_haj")
    # categorie5 = models.Categorie.objects.create(nom_categorie="voyage_organise")
    

    # # Create Voyage instances
    # voyage1 = models.Voyage.objects.create(
    #     titre_voyage = "titre voyage",prix_voyage=10000.0, duree_voyage=5, transport=True, id_hotel=hotel6, id_promotion=promotion1, id_categorie=categorie1
    # )
    # voyage2 = models.Voyage.objects.create(
    #     titre_voyage = "titre voyage",prix_voyage=12000.0, duree_voyage=7, transport=True, id_hotel=hotel5, id_promotion=promotion2, id_categorie=categorie2
    # )
    # voyage3 = models.Voyage.objects.create(
    #     titre_voyage = "titre voyage",prix_voyage=80000.0, duree_voyage=4, transport=False, id_hotel=hotel4, id_promotion=promotion3, id_categorie=categorie3
    # )
    # voyage4 = models.Voyage.objects.create(
    #     titre_voyage = "titre voyage 4",prix_voyage=100800.0, duree_voyage=12, transport=False, id_hotel=hotel4, id_categorie=categorie4
    # )
    # voyage5 = models.Voyage.objects.create(
    #     titre_voyage = "titre voyage 4",prix_voyage=100800.0, duree_voyage=12, transport=False, id_hotel=hotel1, id_categorie=categorie5
    # )
    # voyage6 = models.Voyage.objects.create(
    #     titre_voyage = "titre voyage 4",prix_voyage=100800.0, duree_voyage=12, transport=False, id_hotel=hotel3, id_categorie=categorie5
    # )
    # voyage4.save()
    # voyage5.save()
    # voyage6.save()
    # # Create Commentaire instances
    # commentaire1 = models.Commentaire.objects.create(id_utilisateur = utilisateur1,
    #     text_comment="Great experience!", date_redaction=timezone.now().date(), heure_redaction=timezone.now().time(), evaluation=5, id_voyage=voyage1
    # )
    # commentaire2 = models.Commentaire.objects.create(id_utilisateur = utilisateur2,
    #     text_comment="Wonderful trip!", date_redaction=timezone.now().date(), heure_redaction=timezone.now().time(), evaluation=4, id_voyage=voyage2
    # )
    # commentaire3 = models.Commentaire.objects.create(id_utilisateur = utilisateur3,
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
    # avoir1 = models.Avoir.objects.create(id_voyage=voyage1, id_ville=ville6)
    # avoir2 = models.Avoir.objects.create(id_voyage=voyage2, id_ville=ville5)
    # avoir3 = models.Avoir.objects.create(id_voyage=voyage3, id_ville=ville4)
    # avoir4 = models.Avoir.objects.create(id_voyage=voyage4, id_ville=ville4)
    # avoir5 = models.Avoir.objects.create(id_voyage=voyage5, id_ville=ville1)
    # avoir6 = models.Avoir.objects.create(id_voyage=voyage6, id_ville=ville3)
    # avoir1.save()
    # avoir2.save()
    # avoir3.save()
    # avoir4.save()
    # avoir5.save()
    # avoir6.save()
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
    user_id_session = request.session.get('code_session')
    if user_id_session:
        utilisateur = models.Utilisateur.objects.filter(id_utilisateur=user_id_session).first()
        if utilisateur:
            return render(request, 'user/home.html', {'utilisateur': utilisateur})
    return render(request, 'user/home.html')

def voyageDetails(id_voyage):
    avoir = models.Avoir.objects.filter(id_voyage = id_voyage)
    inclure_instance = models.inclure.objects.filter(id_voyage=id_voyage)
    comment = models.Commentaire.objects.filter(id_voyage = id_voyage).order_by('-date_redaction', '-heure_redaction')
    return avoir, inclure_instance, comment

def voyage_organise(request):
    query = models.Avoir.objects.all()  
    user_id_session = request.session.get('code_session')
    if user_id_session:
        utilisateur = models.Utilisateur.objects.filter(id_utilisateur=user_id_session).first()
        if utilisateur:
            return render(request, 'user/voyage_organise.html', {'query' : query, 'utilisateur': utilisateur})
    return render(request, 'user/voyage_organise.html', {'query' : query})

def voyage_organise_details(request, id_voyage):
    avoir, inclure_instance, comment = voyageDetails(id_voyage)
    user_id_session = request.session.get('code_session')
    if user_id_session:
        utilisateur = models.Utilisateur.objects.filter(id_utilisateur=user_id_session).first()
        if utilisateur:
            return render(request, 'user/voyage_organise_details.html', {'id_voyage' : id_voyage, 'avoir' : avoir, 'inclure' : inclure_instance, 'comments' : comment, 'utilisateur': utilisateur})
    return render(request, 'user/voyage_organise_details.html', {'id_voyage' : id_voyage, 'avoir' : avoir, 'inclure' : inclure_instance, 'comments' : comment})

def paysRelatedToVoyage(ville):
    return models.Avoir.objects.get(id_ville = ville).id_ville.id_pays

def promotions(request):
    query = models.Avoir.objects.select_related(
        'id_voyage__id_hotel__id_ville__id_pays',  # Inclure le pays lié à l'hôtel
        'id_voyage__id_promotion',
        'id_voyage__id_categorie',
        'id_ville__id_pays'  # Inclure le pays lié à la ville
        ).all()
    user_id_session = request.session.get('code_session')
    if user_id_session:
        utilisateur = models.Utilisateur.objects.filter(id_utilisateur=user_id_session).first()
        if utilisateur:
            return render(request, 'user/promotions.html', {'query' : query, 'utilisateur': utilisateur})
    return render(request, 'user/promotions.html', {'query' : query})

def promotions_details(request, id_voyage):  
    avoir, inclure_instance, comment = voyageDetails(id_voyage)
    user_id_session = request.session.get('code_session')
    if user_id_session:
        utilisateur = models.Utilisateur.objects.filter(id_utilisateur=user_id_session).first()
        if utilisateur:
            return render(request, 'user/promotions_details.html', {'id_voyage' : id_voyage, 'utilisateur': utilisateur, 'avoir' : avoir, 'inclure' : inclure_instance, 'comments' : comment})
    return render(request, 'user/promotions_details.html', {'id_voyage' : id_voyage, 'avoir' : avoir, 'inclure' : inclure_instance, 'comments' : comment})

def hotels(request):
    try:
        pays = models.Pays.objects.get(nom_pays='Maroc')
    except models.Pays.DoesNotExist:
        # Handle the case where 'Maroc' does not exist
        pays = None

    if pays:
        villes = models.Ville.objects.filter(id_pays=pays).values_list('id_ville', flat=True)
        query = models.Hotel.objects.filter(id_ville__in=villes)
    else:
        # Handle the case where 'Maroc' does not exist (query would be empty)
        query = []
    user_id_session = request.session.get('code_session')
    if user_id_session:
        utilisateur = models.Utilisateur.objects.filter(id_utilisateur=user_id_session).first()
        if utilisateur:
            return render(request, 'user/hotels.html', {'query': query, 'utilisateur': utilisateur})
    return render(request, 'user/hotels.html', {'query': query})

def hotels_details(request, id_hotel):
    hotel = models.Hotel.objects.filter(id_hotel=id_hotel)
    user_id_session = request.session.get('code_session')
    if user_id_session:
        utilisateur = models.Utilisateur.objects.filter(id_utilisateur=user_id_session).first()
        if utilisateur:
            return render(request, 'user/hotels_details.html', {'hotel' : hotel, 'utilisateur': utilisateur})
    return render(request, 'user/hotels_details.html', {'hotel' : hotel})

def special_turqie(request):
    query = models.Avoir.objects.all()
    user_id_session = request.session.get('code_session')
    if user_id_session:
        utilisateur = models.Utilisateur.objects.filter(id_utilisateur=user_id_session).first()
        if utilisateur:
            return render(request, 'user/special_turqie.html', {'query' :query, 'utilisateur': utilisateur})
    return render(request, 'user/special_turqie.html', {'query' :query})

def special_turqie_details(request, id_voyage):
    avoir, inclure_instance, comment = voyageDetails(id_voyage)
    user_id_session = request.session.get('code_session')
    if user_id_session:
        utilisateur = models.Utilisateur.objects.filter(id_utilisateur=user_id_session).first()
        if utilisateur:
            return render(request, 'user/special_turqie_details.html', {'id_voyage' : id_voyage, 'utilisateur': utilisateur, 'avoir' : avoir, 'inclure' : inclure_instance, 'comments' : comment})
    return render(request, 'user/special_turqie_details.html', {'id_voyage' : id_voyage, 'avoir' : avoir, 'inclure' : inclure_instance, 'comments' : comment})

def special_asie(request):
    query = models.Avoir.objects.all()
    user_id_session = request.session.get('code_session')
    if user_id_session:
        utilisateur = models.Utilisateur.objects.filter(id_utilisateur=user_id_session).first()
        if utilisateur:
            return render(request, 'user/special_asie.html', {'query' :query, 'utilisateur': utilisateur})
    return render(request, 'user/special_asie.html', {'query' :query})

def special_asie_details(request, id_voyage):
    avoir, inclure_instance, comments = voyageDetails(id_voyage)
    user_id_session = request.session.get('code_session')
    if user_id_session:
        utilisateur = models.Utilisateur.objects.filter(id_utilisateur=user_id_session).first()
        if utilisateur:
            return render(request, 'user/special_asie_details.html', {'id_voyage' : id_voyage, 'utilisateur': utilisateur, 'comments' : comments, 'avoir' : avoir, 'inclure' : inclure_instance})
    return render(request, 'user/special_asie_details.html', {'id_voyage' : id_voyage, 'comments' : comments, 'avoir' : avoir, 'inclure' : inclure_instance})

def special_omra(request):
    query = models.Avoir.objects.all()
    user_id_session = request.session.get('code_session')
    if user_id_session:
        utilisateur = models.Utilisateur.objects.filter(id_utilisateur=user_id_session).first()
        if utilisateur:
            return render(request, 'user/special_omra.html', {'query' :query, 'utilisateur': utilisateur})
    return render(request, 'user/special_omra.html', {'query' :query})

def special_omra_details(request, id_voyage):
    avoir, inclure_instance, comment = voyageDetails(id_voyage)
    user_id_session = request.session.get('code_session')
    if user_id_session:
        utilisateur = models.Utilisateur.objects.filter(id_utilisateur=user_id_session).first()
        if utilisateur:
            return render(request, 'user/special_omra_details.html', {'id_voyage' : id_voyage, 'utilisateur': utilisateur, 'avoir' : avoir, 'inclure' : inclure_instance, 'comments' : comment})
    return render(request, 'user/special_omra_details.html', {'id_voyage' : id_voyage, 'avoir' : avoir, 'inclure' : inclure_instance, 'comments' : comment})


def special_haj(request):
    query = models.Avoir.objects.all()
    user_id_session = request.session.get('code_session')
    if user_id_session:
        utilisateur = models.Utilisateur.objects.filter(id_utilisateur=user_id_session).first()
        if utilisateur:
            return render(request, 'user/special_haj.html', {'query' :query, 'utilisateur': utilisateur})
    return render(request, 'user/special_haj.html', {'query' :query})

def special_haj_details(request, id_voyage):
    avoir, inclure_instance, comment = voyageDetails(id_voyage)
    user_id_session = request.session.get('code_session')
    if user_id_session:
        utilisateur = models.Utilisateur.objects.filter(id_utilisateur=user_id_session).first()
        if utilisateur:
            return render(request, 'user/special_haj_details.html', {'id_voyage' : id_voyage, 'utilisateur': utilisateur, 'avoir' : avoir, 'inclure' : inclure_instance, 'comments' : comment})
    return render(request, 'user/special_haj_details.html', {'id_voyage' : id_voyage, 'avoir' : avoir, 'inclure' : inclure_instance, 'comments' : comment})

# comments and like handling
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        elif isinstance(obj, time):
            return obj.isoformat()
        else:
            return super().default(obj)


def retrieve_comments(request):
    try:
        # Retrieve the JSON data from the request
        data = json.loads(request.body.decode('utf-8'))
        print("Received data:", data)  # Add this line for debugging
        
        # Get the Voyage and Utilisateur objects from the database or raise Http404
        voyage = get_object_or_404(models.Voyage, id_voyage=int(data.get('id_voyage', 0)))
        utilisateur = get_object_or_404(models.Utilisateur, id_utilisateur=int(data.get('id_user', 0)))

        # Create a Commentaire object and save it to the database
        comment = models.Commentaire(
            text_comment=data.get('comment', ''),
            date_redaction=timezone.now().date(),
            heure_redaction=timezone.now().time(),
            evaluation=int(data.get('rating', 0)),
            id_utilisateur=utilisateur,
            id_voyage=voyage
        )
        comment.save()
        # Convert the Commentaire object to a dictionary
        new_comment = model_to_dict(comment)
        utilisateur = model_to_dict(utilisateur)
        # Encode the data as a JSON string
        response_data = json.dumps({'success': True, 'new_comment': new_comment, 'utilisateur' : utilisateur}, cls=CustomJSONEncoder)
        # Return a JsonResponse with the data
        return JsonResponse(response_data, safe=False)
    except json.JSONDecodeError as e:
        print("JSON Decode Error:", e)
        # Return a JsonResponse with an error message
        return JsonResponse(json.dumps({'success': False, 'error': str(e)}), safe=False)

def retrieve_likes(request):
    data = json.loads(request.body.decode('utf-8'))
    print("Received data:", data)  # Add this line for debugging
    
    utilisateur = models.Utilisateur.objects.get(id_utilisateur=data.get('id_user', 0))
    voyage = models.Voyage.objects.get(id_voyage=data.get('id_voyage', 0))
    if models.Aimer.objects.filter(id_utilisateur_1=utilisateur, id_voyage=voyage):
        existe = True
    else : existe = False
    print("Received data:", data)  # Add this line for debugging
    return JsonResponse(json.dumps({'fetch': True, 'id_user' : data.get('id_user', 0), 'id_voyage' : data.get('id_voyage', 0), 'existe' : existe  }), safe=False)

def delete_like(request):
    data = json.loads(request.body.decode('utf-8'))
    print("Received del data:", data)  # Add this line for debugging
    
    utilisateur = models.Utilisateur.objects.get(id_utilisateur=data.get('id_user', 0))
    voyage = models.Voyage.objects.get(id_voyage=data.get('id_voyage', 0))
    models.Aimer.objects.filter(id_utilisateur_1=utilisateur, id_voyage=voyage).delete()
    return JsonResponse(json.dumps({'existe' : False, 'delete': True}), safe=False)


def add_like(request):
    data = json.loads(request.body.decode('utf-8'))
    print("Received add data:", data)  # Add this line for debugging
    
    utilisateur = models.Utilisateur.objects.get(id_utilisateur=data.get('id_user', 0))
    voyage = models.Voyage.objects.get(id_voyage=data.get('id_voyage', 0))
    aimer = models.Aimer(id_utilisateur_1=utilisateur, id_voyage=voyage)
    aimer.save()
    return JsonResponse(json.dumps({'existe' : True, 'add': True}), safe=False)

# admin views
def admin_view(request):
    if request.session.get('est_admin',None) != None:
        return render(request, 'admin_pages/dashboard.html', {})
    else:
        return redirect('login')
def pays_gestion(request):
    if request.session.get('est_admin',None) != None:
        pays = models.Pays.objects.all()
        return render(request, 'admin_pages/pays_gestion.html', {'pays' : pays})
    else:
        return redirect('login')

def villes_gestion(request):
    if request.session.get('est_admin',None) != None:
        villes = models.Ville.objects.all()
        return render(request,'admin_pages/villes_gestion.html',{'villes' : villes})
    else:
        return redirect('login')

def commentaires_gestion(request):
    if request.session.get('est_admin',None) != None:
        commentaires = models.Commentaire.objects.all()
        return render(request, 'admin_pages/commentaires_gestion.html',{'commentaires' : commentaires})
    else:
        return redirect('login')

def notifications_gestion(request):
    if request.session.get('est_admin',None) != None:
        notifications = models.Notification.objects.all()
        return render(request, 'admin_pages/notifications_gestion.html',{'notifications' : notifications})
    else:
        return redirect('login')

def vols_gestion(request):
    if request.session.get('est_admin',None) != None:
        vols = models.Vol.objects.all()
        return render(request, 'admin_pages/vols_gestion.html',{'vols' : vols})
    else:
        return redirect('login')
def promotions_gestion(request):
    if request.session.get('est_admin',None) != None:
        promotions = models.Promotion.objects.all()
        return render(request, 'admin_pages/promotions_gestion.html',{'promotions' : promotions})
    else:
        return redirect('login')
def hotels_gestion(request):
    if request.session.get('est_admin',None) != None:
        hotels = models.Hotel.objects.all()
        return render(request, 'admin_pages/hotels_gestion.html',{'hotels' : hotels})
    else:
        return redirect('login')
    
def voyages_gestion(request):
    if request.session.get('est_admin',None) != None:
        voyages = models.Voyage.objects.all()
        return render(request, 'admin_pages/voyages_gestion.html',{'voyages' : voyages})
    else:
        return redirect('login')
    
def dashboard_gestion(request):
    if request.session.get('est_admin', None) != None:
        nbr_reservations = models.ReserverVoyage.objects.count()
        reservations = models.ReserverVoyage.objects.all()
        total_price = models.ReserverVoyage.objects.aggregate(Sum('id_voyage__prix_voyage'))['id_voyage__prix_voyage__sum']
        client_nb = models.Utilisateur.objects.filter(est_admin = 0).count()
        nb_voyage = models.Voyage.objects.count()
        Satisfaction = models.Commentaire.objects.aggregate(Sum('evaluation'))['evaluation__sum'] / models.Commentaire.objects.aggregate(Count('evaluation'))['evaluation__count']
        return render(request, 'admin_pages/dashboard.html',{'reservations' : reservations,'Satisfaction' : Satisfaction,'nb_voyages': nb_voyage, 'reservations_nbr' : nbr_reservations, 'revenue' : total_price,'client_nb' : client_nb})
    else:
        return redirect('login')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = None
        for usr in models.Utilisateur.objects.all():
            if password == usr.mot_d_passe and email == usr.email:
                user = usr
                break

        if user is not None:
            if not user.est_admin:
                request.session['code_session'] = user.id_utilisateur
                # return redirect('profile', user.id_utilisateur)
                return redirect('/')
            else:
                request.session['est_admin'] = user.id_utilisateur
                return redirect('dashboard_gestion')

        error_message = "Identifiants incorrects. Veuillez réessayer."
        return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html', {})

        
from django.shortcuts import redirect

def logout(request):
    if 'code_session' in request.session:
        del request.session['code_session']
    elif 'est_admin' in request.session:
        del request.session['est_admin']
    return redirect('/')


def profile_view(request, user_id):
    if request.session.get('code_session',None) == user_id:
        utilisateur = models.Utilisateur.objects.get(id_utilisateur=user_id)
        return render(request, 'user/profile.html', {'utilisateur': utilisateur})
    else:
        return redirect('login')


def registration(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        num_tele = request.POST.get('num_telephone')
        passwd = request.POST.get('mot_d_passe')
        uploaded_image = request.FILES.get('path_img_profile')
        print(nom+' '+prenom+' '+email+' '+num_tele+' '+passwd+uploaded_image.name )
        if nom and prenom and email and num_tele and passwd and uploaded_image:

            image_filename = uploaded_image.name
            image_path = f'./app/static/assets/profile_imgs/{image_filename}'

            with open(image_path, 'wb') as destination:
                for chunk in uploaded_image.chunks():
                    destination.write(chunk)

            user = models.Utilisateur.objects.create(
                path_img_profile=image_filename,
                est_admin=0,
                nom=nom,
                prenom=prenom,
                email=email,
                num_telephone=num_tele,
                mot_d_passe=passwd
            )
            user.save()

            # Redirect to a success page or profile view
            return redirect('profile', user.id_utilisateur)

    return render(request, 'registration.html')


def supp_voyage(request,id_voyage):
    voyage = models.Voyage.objects.get(id_voyage = id_voyage)
    voyage.delete()
    voyages = models.Voyage.objects.all()
    message_supp = "Voyage id: "+str(id_voyage)+" est supprimée!"
    return  render(request,'admin_pages/voyages_gestion.html',{'voyages' : voyages,'messageSupp' : message_supp})

def modif_voyage(request,id_voyage):
    voyage = get_object_or_404(models.Voyage, id_voyage=id_voyage)
    voyages = models.Voyage.objects.all()
    if request.method == 'POST':
        form = VoyageModificationForm(request.POST,instance = voyage)
        if form.is_valid():
            form.save()
            message = "Voyage id: "+str(id_voyage)+" est modifiée!"
            return  render(request,'admin_pages/voyages_gestion.html',{'voyages' : voyages,'messageEdit' : message})
            #redirect('admin_page/voyages/')
    else:    
        
        form = VoyageModificationForm(instance = voyage)
        return  render(request,'admin_pages/voyages_gestion.html',{'voyages' : voyages,'voyage' : voyage,'form_modif':form})
        
def ajout_voyage(request):
    if request.method == 'POST':
        form = VoyageAjoutForm(request.POST)
        if form.is_valid():
            #form.save()
            titre_voyage = form.cleaned_data['titre_voyage']
            prix_voyage = form.cleaned_data['prix_voyage']
            duree_voyage = form.cleaned_data['duree_voyage']
            transport = form.cleaned_data['transport']
            id_hotel = form.cleaned_data['id_hotel']
            #hotel = models.Hotel.objects.get(id_hotel = id_hotel)
            id_promotion = form.cleaned_data['id_promotion']
            id_categorie = form.cleaned_data['id_categorie']
            #strin = titre_voyage+" "+str(prix_voyage)+" "+str(duree_voyage)+" "+str(transport)+" "+str(id_hotel)+" "+str(id_promotion)+" "+str(id_categorie)
            #"return HttpResponse(strin)
            voyage = models.Voyage.objects.create(id_promotion = id_promotion,titre_voyage = titre_voyage,prix_voyage=prix_voyage,duree_voyage=duree_voyage,transport=transport,id_hotel=id_hotel,id_categorie=id_categorie)
            #voyage.id_promotion.set(id_promotion)
            voyage.save()
            voyage.id_promotion = id_promotion
            voyage.save()
            return voyages_gestion(request)
    else:    
        voyages = models.Voyage.objects.all()
        form = VoyageAjoutForm()
        return  render(request,'admin_pages/voyages_gestion.html',{'voyages' : voyages,'form_ajout':form})
        
def supp_hotel(request,id_hotel):
    hotel = models.Hotel.objects.get(id_hotel = id_hotel)
    hotel.delete()
    hotels = models.Hotel.objects.all()
    message_supp = "Hotels id: "+str(id_hotel)+" est supprimée!"
    return  render(request,'admin_pages/hotels_gestion.html',{'hotels' : hotels,'messageSupp' : message_supp})

def modif_hotel(request,id_hotel):
    hotel = get_object_or_404(models.Hotel, id_hotel=id_hotel)
    hotels = models.Hotel.objects.all()
    if request.method == 'POST':
        form = HotelModificationForm(request.POST,instance = hotel)
        if form.is_valid():
            form.save()
            message = "Voyage id: "+str(id_hotel)+" est modifiée!"
            return  render(request,'admin_pages/hotels_gestion.html',{'hotels' : hotels,'messageEdit' : message})
            #redirect('admin_page/voyages/')
    else:    
        form = HotelModificationForm(instance = hotel)
        return  render(request,'admin_pages/hotels_gestion.html',{'hotels' : hotels,'hotel' : hotel,'form_modif':form})

def ajout_hotel(request):
    hotels = models.Hotel.objects.all()
    if request.method == 'POST':
        form = HotelAjoutForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Nouvelle hotel est ajouté avec succée!"
            return  render(request,'admin_pages/hotels_gestion.html',{'hotels' : hotels,'messageEdit' : message})
            #redirect('admin_page/voyages/')
    else:    
        form = HotelAjoutForm()
        return  render(request,'admin_pages/hotels_gestion.html',{'hotels' : hotels,'form_ajout':form})

def supp_promotion(request,id_promotion):
    promotion = models.Promotion.objects.get(id_promotion = id_promotion)
    promotion.delete()
    promotions = models.Promotion.objects.all()
    message_supp = "promotions id: "+str(id_promotion)+" est supprimée!"
    return  render(request,'admin_pages/promotions_gestion.html',{'promotions' : promotions,'messageSupp' : message_supp})

def modif_promotion(request,id_promotion):
    promotion = get_object_or_404(models.Promotion, id_promotion=id_promotion)
    promotions = models.Promotion.objects.all()
    if request.method == 'POST':
        form = PromotionModificationForm(request.POST,instance = promotion)
        if form.is_valid():
            form.save()
            message = "Promotion id: "+str(id_promotion)+" est modifiée!"
            return  render(request,'admin_pages/promotions_gestion.html',{'promotions' : promotions,'messageEdit' : message})
            #redirect('admin_page/voyages/')
    else:    
        form = PromotionModificationForm(instance = promotion)
        return  render(request,'admin_pages/promotions_gestion.html',{'promotions' : promotions,'promotion' : promotion,'form_modif':form})

def ajout_promotion(request):
    promotions = models.Promotion.objects.all()
    if request.method == 'POST':
        form = PromotionAjoutForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Nouvelle promotion est ajouté avec succée!"
            return  render(request,'admin_pages/promotions_gestion.html',{'promotions' : promotions,'messageEdit' : message})
            #redirect('admin_page/voyages/')
    else:    
        form = PromotionAjoutForm()
        return  render(request,'admin_pages/promotions_gestion.html',{'promotions' : promotions,'form_ajout':form})

def supp_vol(request,id_vol):
    vol = models.Vol.objects.get(id_vol = id_vol)
    vol.delete()
    vols = models.Vol.objects.all()
    message_supp = "vols id: "+id_vol+" est supprimée!"
    return  render(request,'admin_pages/vols_gestion.html',{'vols' : vols,'messageSupp' : message_supp})

def modif_vol(request,id_vol):
    vol = get_object_or_404(models.Vol, id_vol=id_vol)
    vols = models.Vol.objects.all()
    if request.method == 'POST':
        form = VolModificationForm(request.POST,instance = vol)
        if form.is_valid():
            form.save()
            message = "vol id: "+id_vol+" est modifiée!"
            return  render(request,'admin_pages/vols_gestion.html',{'vols' : vols,'messageEdit' : message})
            #redirect('admin_page/voyages/')
    else:    
        form = VolModificationForm(instance = vol)
        return  render(request,'admin_pages/vols_gestion.html',{'vols' : vols,'vol' : vol,'form_modif':form})

def ajout_vol(request):
    vols = models.Vol.objects.all()
    if request.method == 'POST':
        form = VolAjoutForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Nouvelle vol est ajouté avec succée!"
            return  render(request,'admin_pages/vols_gestion.html',{'vols' : vols,'messageEdit' : message})
            #redirect('admin_page/voyages/')
    else:    
        form = VolAjoutForm()
        return  render(request,'admin_pages/vols_gestion.html',{'vols' : vols,'form_ajout':form})

def supp_ville(request,id_ville):
    ville = models.Ville.objects.get(id_ville = id_ville)
    ville.delete()
    villes = models.Ville.objects.all()
    message_supp = "ville id: "+str(id_ville)+" est supprimée!"
    return  render(request,'admin_pages/villes_gestion.html',{'villes' : villes,'messageSupp' : message_supp})

def ajout_ville(request):
    villes = models.Ville.objects.all()
    if request.method == 'POST':
        form = VilleAjoutForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Nouvelle ville est ajouté avec succée!"
            return  render(request,'admin_pages/villes_gestion.html',{'villes' : villes,'messageEdit' : message})
            #redirect('admin_page/voyages/')
    else:    
        form = VilleAjoutForm()
        return  render(request,'admin_pages/villes_gestion.html',{'villes' : villes,'form_ajout':form})
    

def supp_pays(request,id_pays):
    pays = models.Pays.objects.get(id_pays = id_pays)
    pays.delete()
    pays = models.Pays.objects.all()
    message_supp = "pays id: "+str(id_pays)+" est supprimée!"
    return  render(request,'admin_pages/pays_gestion.html',{'pays' : pays,'messageSupp' : message_supp})
def modif_pays(request,id_pays):
    pays = get_object_or_404(models.Pays, id_pays=id_pays)
    if request.method == 'POST':
        form = PaysAjoutForm(request.POST,instance=pays)
        if form.is_valid():
            form.save()
            message = "Nouvelle pays est ajouté avec succée!"
            return  render(request,'admin_pages/pays_gestion.html',{'pays' : pays,'messageEdit' : message})
            #redirect('admin_page/voyages/')
    else:    
        form = PaysAjoutForm(instance = pays)
        return  render(request,'admin_pages/pays_gestion.html',{'pays' : pays,'form_ajout':form})

def ajout_pays(request):
    pays = models.Pays.objects.all()
    if request.method == 'POST':
        form = PaysAjoutForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Nouvelle pays est ajouté avec succée!"
            return  render(request,'admin_pages/pays_gestion.html',{'pays' : pays,'messageEdit' : message})
            #redirect('admin_page/voyages/')
    else:    
        form = PaysAjoutForm()
        return  render(request,'admin_pages/pays_gestion.html',{'pays' : pays,'form_ajout':form})


def supp_commentaire(request,id_commentaire):
    c = models.Commentaire.objects.get(id_comment = id_commentaire)
    c.delete()
    commentaires = models.Commentaire.objects.all()
    message_supp = "Commentaire id: "+str(id_commentaire)+" est supprimée!"
    return  render(request,'admin_pages/commentaires_gestion.html',{'commentaires' : commentaires,'messageSupp' : message_supp})