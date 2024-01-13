from django.forms import model_to_dict
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, request
from django.db.models import *
from app.forms import PaysForm
from . import models
from datetime import datetime
from decimal import Decimal
from django.utils import timezone
from django.http import JsonResponse
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
    return render(request, 'visitor/home.html')


def voyageDetails(id_voyage):
    avoir = models.Avoir.objects.filter(id_voyage = id_voyage)
    inclure_instance = models.inclure.objects.filter(id_voyage=id_voyage)
    comment = models.Commentaire.objects.filter(id_voyage = id_voyage).order_by('-date_redaction', '-heure_redaction')
    return avoir, inclure_instance, comment

def voyage_organise(request):
    query = models.Avoir.objects.all()  
    return render(request, 'visitor/voyage_organise.html', {'query' : query})

def voyage_organise_details(request, id_voyage):
    avoir, inclure_instance, comment = voyageDetails(id_voyage)
    return render(request, 'visitor/voyage_organise_details.html', {'id_voyage' : id_voyage, 'avoir' : avoir, 'inclure' : inclure_instance, 'comments' : comment})

def paysRelatedToVoyage(ville):
    return models.Avoir.objects.get(id_ville = ville).id_ville.id_pays

def promotions(request):
    query = models.Avoir.objects.select_related(
        'id_voyage__id_hotel__id_ville__id_pays',  # Inclure le pays lié à l'hôtel
        'id_voyage__id_promotion',
        'id_voyage__id_categorie',
        'id_ville__id_pays'  # Inclure le pays lié à la ville
        ).all()
    return render(request, 'visitor/promotions.html', {'query' : query})

def promotions_details(request, id_voyage):  
    avoir, inclure_instance, comment = voyageDetails(id_voyage)
    return render(request, 'visitor/promotions_details.html', {'id_voyage' : id_voyage, 'avoir' : avoir, 'inclure' : inclure_instance, 'comments' : comment})

def hotels(request):
    query = models.Hotel.objects.all()
    return render(request, 'visitor/hotels.html', {'query' :query})

def hotels_details(request, id_hotel):
    hotels = models.Hotel.objects.filter(id_hotel=id_hotel)
    return render(request, 'visitor/hotels_details.html', {'hotels' : hotels})

def special_turqie(request):
    query = models.Avoir.objects.all()
    return render(request, 'visitor/special_turqie.html', {'query' :query})

def special_turqie_details(request, id_voyage):
    avoir, inclure_instance, comment = voyageDetails(id_voyage)
    return render(request, 'visitor/special_turqie_details.html', {'id_voyage' : id_voyage, 'avoir' : avoir, 'inclure' : inclure_instance, 'comments' : comment})


def special_asie(request):
    # ville = models.Ville.filter(nom_ville='tokyo')
    query = models.Avoir.objects.all()
    # print(query)
    # imageville = models.ImageVille.objects.filter(ville=query.Avoir.id_ville).first()
    # imageville =1
    # return render(request, 'visitor/special_asie.html', {'query' :query, 'imageville' : imageville})
    return render(request, 'visitor/special_asie.html', {'query' :query})

def special_asie_details(request, id_voyage):
    avoir, inclure_instance, comments = voyageDetails(id_voyage)
    return render(request, 'visitor/special_asie_details.html', {'id_voyage' : id_voyage, 'comments' : comments, 'avoir' : avoir, 'inclure' : inclure_instance})

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        elif isinstance(obj, time):
            return obj.isoformat()
        else:
            return super().default(obj)

def special_asie_comments(request):
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
            date_redaction=timezone.now().date().isoformat(),
            heure_redaction=timezone.now().time().isoformat(),
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



def special_omra(request):
    query = models.Avoir.objects.all()
    return render(request, 'visitor/special_omra.html', {'query' :query})

def special_omra_details(request, id_voyage):
    avoir, inclure_instance, comment = voyageDetails(id_voyage)
    return render(request, 'visitor/special_omra_details.html', {'id_voyage' : id_voyage, 'avoir' : avoir, 'inclure' : inclure_instance, 'comments' : comment})


def special_haj(request):
    query = models.Avoir.objects.all()
    return render(request, 'visitor/special_haj.html', {'query' :query})

def special_haj_details(request, id_voyage):
    avoir, inclure_instance, comment = voyageDetails(id_voyage)
    return render(request, 'visitor/special_haj_details.html', {'id_voyage' : id_voyage, 'avoir' : avoir, 'inclure' : inclure_instance, 'comments' : comment})


# admin views
def admin_view(request):
    return render(request, 'admin_pages/dashboard.html', {})

def pays_gestion(request):
    if request.method == 'POST':
        form = PaysForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('success')  # Redirect to a success page
            return render(request, 'admin_pages/pays_gestion.html', {'form' : form, 'form_msg' : 'succes'})  # Redirect to a success page
    else:
        form = PaysForm()
    pays = models.Pays.objects.all()
    return render(request, 'admin_pages/pays_gestion.html', {'form': form, 'pays' : pays})
def villes_gestion(request):
    villes = models.Ville.objects.all()
    return render(request,'admin_pages/villes_gestion.html',{'villes' : villes})

def commentaires_gestion(request):
    commentaires = models.Commentaire.objects.all()
    return render(request, 'admin_pages/commentaires_gestion.html',{'commentaires' : commentaires})

def notifications_gestion(request):
    notifications = models.Notification.objects.all()
    return render(request, 'admin_pages/notifications_gestion.html',{'notifications' : notifications})

def vols_gestion(request):
    vols = models.Vol.objects.all()
    return render(request, 'admin_pages/vols_gestion.html',{'vols' : vols})

def promotions_gestion(request):
    promotions = models.Promotion.objects.all()
    return render(request, 'admin_pages/promotions_gestion.html',{'promotions' : promotions})
def hotels_gestion(request):
    hotels = models.Hotel.objects.all()
    return render(request, 'admin_pages/hotels_gestion.html',{'hotels' : hotels})
def voyages_gestion(request):
    voyages = models.Voyage.objects.all()
    return render(request, 'admin_pages/voyages_gestion.html',{'voyages' : voyages})
def dashboard_gestion(request):
    nbr_reservations = models.ReserverVoyage.objects.count()
    reservations = models.ReserverVoyage.objects.all()
    total_price = models.ReserverVoyage.objects.aggregate(Sum('id_voyage__prix_voyage'))['id_voyage__prix_voyage__sum']
    client_nb = models.Utilisateur.objects.filter(est_admin = 0).count()
    nb_voyage = models.Voyage.objects.count()
    Satisfaction = models.Commentaire.objects.aggregate(Sum('evaluation'))['evaluation__sum'] / models.Commentaire.objects.aggregate(Count('evaluation'))['evaluation__count']
    return render(request, 'admin_pages/dashboard.html',{'reservations' : reservations,'Satisfaction' : Satisfaction,'nb_voyages': nb_voyage, 'reservations_nbr' : nbr_reservations, 'revenue' : total_price,'client_nb' : client_nb})

