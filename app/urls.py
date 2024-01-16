from django.urls import path
from . import views

# app_name = 'mon_app'

urlpatterns = [
    path('', views.home, name="home"),
    
    path('voyage_organise/', views.voyage_organise, name="voyage_organise"),
    path('voyage_organise/details/<int:id_voyage>/', views.voyage_organise_details, name="voyage_organise_details"),
    
    path('promotions/', views.promotions, name="promotions"),
    path('promotions/details/<int:id_voyage>/', views.promotions_details, name="promotions_details"),
    
    path('hotels/', views.hotels, name="hotels"),
    path('hotels_details/<int:id_hotel>/', views.hotels_details, name="hotels_details"),
    
    path('special_turqie/', views.special_turqie, name="special_turqie"),
    path('special_turqie/details/<int:id_voyage>/', views.special_turqie_details, name="special_turqie_details"),
    
    path('special_asie/', views.special_asie, name="special_asie"),
    path('special_asie/like/', views.special_asie_like, name="special_asie_like"),
    path('special_asie/delete/', views.special_asie_like_del, name="special_asie_like_del"),
    path('special_asie/add/', views.special_asie_like_add, name="special_asie_like_add"),
    path('special_asie/details/<int:id_voyage>/', views.special_asie_details, name="special_asie_details"),
    path('special_asie/details/comments/', views.special_asie_comments, name="special_asie_comments"),
    
    path('special_omra/', views.special_omra, name="special_omra"),
    path('special_omra_details/<int:id_voyage>/', views.special_omra_details, name="special_omra_details"),
    
    path('special_haj/', views.special_haj, name="special_haj"),
    path('special_haj/details/<int:id_voyage>/', views.special_haj_details, name="special_haj_details"),

    # admin urls
    path('admin_page/', views.dashboard_gestion, name="admin"),
    path('admin_page/pays/', views.pays_gestion, name="pays_gestion"),
    path('admin_page/villes/', views.villes_gestion, name="villes_gestion"),
    path('admin_page/commentaires/', views.commentaires_gestion, name="commentaires_gestion"),
    path('admin_page/notifications/', views.notifications_gestion, name="notifications_gestion"),
    path('admin_page/vols/', views.vols_gestion, name="vols_gestion"),
    path('admin_page/promotions/', views.promotions_gestion, name="promotions_gestion"),
    path('admin_page/hotels/', views.hotels_gestion, name="hotels_gestion"),
    path('admin_page/voyages/', views.voyages_gestion, name="voyages_gestion"),
    path('admin_page/dashboard/', views.dashboard_gestion, name="dashboard_gestion"),
    # path('login/', views.login, name="login"),
    # path('registration/', views.registration, name="registration"),
    # path('client/profile/<int:user_id>/', views.profile_view, name='profile'),
    # path('logout/', views.logout, name='logout'),

   # path('registration/', views.user_registration, name="registration_login"),
   
    path('admin_login/', views.admin_login, name='admin_login'),
    path('client_login/', views.client_login, name='client_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('client_dashboard/', views.client_dashboard, name='client_dashboard'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('client_logout/', views.client_logout, name='client_logout'),
]
