from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('/voyage_organise', views.voyage_organise, name="voyage_organise"),
]
