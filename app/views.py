from django.shortcuts import render
from django.http import HttpResponse,request
from . import models
def home (request):
    pays = models.Pays.objects.create(nom_pays = "Maroc")
    ville = models.Ville.objects.create(nom_ville ="Agadir",id_pays = pays.id_pays)
    hotel = models.Hotel.objects.create(prix_nuit=250,type_chambre="Deluxe",n_chambreDispo=3,nom_hotel="AL Sahara",id_ville=ville.id_ville)
    voyage = models.Voyage.objects.create(prix_voyage=1500,duree_voyage=7,transport=True,id_hotel=hotel.id_hotel,)
    return render(request, 'home.html', {})


    