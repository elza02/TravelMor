from django.urls import path
from . import views

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
    path('likes/retrieve/', views.retrieve_likes, name="retrieve_likes"),
    path('likes/delete/', views.delete_like, name="delete_like"),
    path('likes/add/', views.add_like, name="add_like"),
    path('special_asie/details/<int:id_voyage>/', views.special_asie_details, name="special_asie_details"),
    path('comments/retrieve/', views.retrieve_comments, name="retrieve_comments"),
    
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
    path('admin_page/utilisateurs/', views.utilisateurs_gestion, name="utilisateurs_gestion"),
    path('admin_page/notification/', views.notification_gestion, name="notification_gestion"),
    
    
    path('registration/', views.registration, name="registration"),
    path('profile/<int:user_id>/', views.profile_view, name='profile'),
    
    path('admin_page/voyages/supp_voyage/<int:id_voyage>/', views.supp_voyage, name='supp_voyage'),
    path('admin_page/voyages/modif_voyage/<int:id_voyage>/', views.modif_voyage, name='modif_voyage'),
    path('admin_page/voyages/ajout_voyage/', views.ajout_voyage, name='ajout_voyage'),
    path('admin_page/voyages/associer_vol_voyage/<str:id_vol>/<int:id_voyage>/', views.associer_vol_voyage, name='associer_vol_voyage'),
    path('admin_page/hotels/supp_hotel/<int:id_hotel>/', views.supp_hotel, name='supp_hotel'),
    path('admin_page/hotels/modif_hotel/<int:id_hotel>/', views.modif_hotel, name='modif_hotel'),
    path('admin_page/hotels/ajout_hotel/', views.ajout_hotel, name='ajout_hotel'),
    path('admin_page/promotions/supp_promotion/<int:id_promotion>/', views.supp_promotion, name='supp_promotion'),
    path('admin_page/promotions/modif_promotion/<int:id_promotion>/', views.modif_promotion, name='modif_promotion'),
    path('admin_page/promotions/ajout_promotion/', views.ajout_promotion, name='ajout_promotion'),
    path('admin_page/vols/supp_vol/<str:id_vol>/', views.supp_vol, name='supp_vol'),
    path('admin_page/vols/modif_vol/<str:id_vol>/', views.modif_vol, name='modif_vol'),
    path('admin_page/vols/ajout_vol/', views.ajout_vol, name='ajout_vol'),
    path('admin_page/villes/supp_ville/<int:id_ville>/', views.supp_ville, name='supp_ville'),
    path('admin_page/villes/ajout_ville/', views.ajout_ville, name='ajout_ville'),
    path('admin_page/pays/supp_pays/<int:id_pays>/', views.supp_pays, name='supp_pays'),
    path('admin_page/pays/modif_pays/<int:id_pays>/', views.modif_pays, name='modif_pays'),
    path('admin_page/pays/ajout_pays/', views.ajout_pays, name='ajout_pays'),
    path('admin_page/commentaires/supp_commentaire/<int:id_commentaire>/', views.supp_commentaire, name='supp_commentaire'),
    path('admin_page/utilisateurs/ajout_utilisateur/', views.ajout_utilisateur, name='ajout_utilisateur'),
    path('admin_page/utilisateurs/supp_utilisateur/<int:id_utilisateur>/', views.supp_utilisateur, name='supp_utilisateur'),
    path('admin_page/utilisateurs/modif_utilisateur/<int:id_utilisateur>/', views.modif_utilisateur, name='modif_utilisateur'),
    path('notifier/', views.notifier, name='notifier'),
    path('admin_page/notification/admin_page/notifications/supp_notification/<int:id_notification>/', views.supp_notification, name='supp_notification'),
    path('admin_page/notification/admin_page/notifications/modif_notification/<int:id_notification>/', views.modif_notification, name='modif_notification'),
    #login/logout
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    path('paiement/<str:id_vol>/', views.paiement, name='paiement'),
]
