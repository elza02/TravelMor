from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    
    path('voyage_organise', views.voyage_organise, name="voyage_organise"),
    
    path('voyage_organise_details/<int:id_voyage>/', views.voyage_organise_details, name="voyage_organise_details"),
    path('promotions', views.promotions, name="promotions"),
    
    path('promotions_details/<int:id_voyage>/', views.promotions_details, name="promotions_details"),
    path('hotels/', views.hotels, name="hotels"),
    
    path('hotels_details/<int:id_voyage>/', views.hotels_details, name="hotels_details"),
    path('special_turqie/', views.special_turqie, name="special_turqie"),
    
    path('special_asie/', views.special_asie, name="special_asie"),
    path('special_asie_details/<int:id_voyage>/', views.special_asie_details, name="special_asie_details"),
    
    path('special_omra/', views.special_omra, name="special_omra"),
    path('special_omra_details/<int:id_voyage>/', views.special_omra_details, name="special_omra_details"),
    
    path('special_haj/', views.special_haj, name="special_haj"),
    path('special_haj_details/<int:id_voyage>/', views.special_haj_details, name="special_haj_details"),
]
