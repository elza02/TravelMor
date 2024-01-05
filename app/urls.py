from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('voyage_organise', views.voyage_organise, name="voyage_organise"),
    path('voyage_organise_details/<int:id_voyage>/', views.voyage_organise_details, name="voyage_organise_details"),
    path('promotions', views.promotions, name="promotions"),
    path('promotions_details/<int:id_voyage>/', views.promotions, name="promotions_details"),
]
