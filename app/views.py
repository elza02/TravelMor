from django.shortcuts import render
from django.http import HttpResponse,request
# from models import *
def home (request):
    
    return render(request, 'home.html', {})


# if __name__ == "__main__":
#     pays = Pays.objects.create("Maroc")
#     ville = Ville.objects.create("Agadir",pays.id_pays)
#     voyage = Voyage.objects.create(1500,7,)