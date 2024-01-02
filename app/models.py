from django.db import models

class Utilisateur(models.Model):
    id_utilisateur_1 = models.IntegerField(primary_key=True)
    est_admin = models.BooleanField()
    nom = models.CharField(max_length=15)
    prenom = models.CharField(max_length=15)
    num_telephone = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    mot_d_passe = models.CharField(max_length=10)
    nom_utilisateur = models.CharField(max_length=50)

class Notification(models.Model):
    id_notification = models.IntegerField(primary_key=True)
    date_notif = models.CharField(max_length=50)
    type = models.CharField(max_length=15)
    heure_d_notif = models.TimeField()

class Promotion(models.Model):
    id_promotion = models.IntegerField(primary_key=True)
    date_d_promo = models.DateField()
    date_f_promo = models.DateField()
    heure_d_promos = models.TimeField()
    heure_f_promos = models.TimeField()
    pourcentage = models.DecimalField(max_digits=4, decimal_places=2)

class Categorie(models.Model):
    id_categorie = models.IntegerField(primary_key=True)
    designation_categorie = models.CharField(max_length=50)

class Pays(models.Model):
    id_pays = models.IntegerField(primary_key=True)
    nom_pays = models.CharField(max_length=50)

class Ville(models.Model):
    id_ville = models.IntegerField(primary_key=True)
    id_pays = models.ForeignKey(Pays, on_delete=models.CASCADE)

class Hotel(models.Model):
    id_hotel = models.CharField(max_length=50, primary_key=True)
    nom_hotel = models.CharField(max_length=50)

class Image(models.Model):
    id_images = models.IntegerField(primary_key=True)
    path_image = models.CharField(max_length=50)

class ImagesVille(models.Model):
    id_images = models.ForeignKey(Image, on_delete=models.CASCADE, primary_key=True)
    id_ville = models.ForeignKey(Ville, on_delete=models.CASCADE)

class ImagesHotel(models.Model):
    id_images = models.ForeignKey(Image, on_delete=models.CASCADE, primary_key=True)
    id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

class Voyage(models.Model):
    id_voyage = models.IntegerField(primary_key=True)
    prix_voyage = models.CharField(max_length=50)
    id_promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    id_categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

class Commentaire(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    text_comment = models.CharField(max_length=150)
    date_redaction = models.DateField()
    heure_redaction = models.TimeField()
    evaluation = models.IntegerField()
    id_voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)

class Recevoir(models.Model):
    id_utilisateur_1 = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    id_notification = models.ForeignKey(Notification, on_delete=models.CASCADE, primary_key=True)

class Reserve(models.Model):
    id_utilisateur_1 = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    id_voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE, primary_key=True)

class Comporte(models.Model):
    id_ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, primary_key=True)

class Avoir(models.Model):
    id_voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    id_ville = models.ForeignKey(Ville, on_delete=models.CASCADE, primary_key=True)
