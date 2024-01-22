from django.db import models

class Notification(models.Model):
    id_notification = models.AutoField(primary_key=True)
    date_notif = models.CharField(max_length=50)
    type = models.CharField(max_length=15)
    heure_d_notif = models.TimeField()
    content = models.CharField(max_length=100, null = True)

class Promotion(models.Model):
    id_promotion = models.AutoField(primary_key=True)
    date_d_promo = models.DateField()
    date_f_promo = models.DateField()
    heure_d_promos = models.TimeField()
    heure_f_promos = models.TimeField()
    pourcentage = models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return f'{self.pourcentage}'
class Categorie(models.Model):
    id_categorie = models.AutoField(primary_key=True)
    nom_categorie = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nom_categorie}"

class Pays(models.Model):
    id_pays = models.AutoField(primary_key=True)
    nom_pays = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nom_pays}"
class Ville(models.Model):
    id_ville = models.AutoField(primary_key=True)
    nom_ville = models.CharField(max_length=50)
    id_pays = models.ForeignKey(Pays, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom_ville}"
class Hotel(models.Model):
    id_hotel = models.AutoField(primary_key=True)
    prix_nuit = models.DecimalField(max_digits=15, decimal_places=2)
    type_chambre = models.CharField(max_length=50)
    type_hotel = models.IntegerField() #c'est le nbr etoile d'hotel 
    n_chambreDispo = models.IntegerField()
    petit_dejeuner = models.BooleanField(default=False)
    nom_hotel = models.CharField(max_length=50)
    id_ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom_hotel}"

class Image(models.Model):
    id_images = models.AutoField(primary_key=True)
    path_image = models.CharField(max_length=50, unique=True)

class ImageVille(models.Model):
    id_images = models.ForeignKey(Image, on_delete=models.CASCADE)
    id_ville = models.ForeignKey(Ville, on_delete=models.CASCADE)

class ImageHotel(models.Model):
    id_images = models.ForeignKey(Image, on_delete=models.CASCADE)
    id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

class Vol(models.Model):
    id_vol = models.CharField(primary_key=True, max_length=50)
    date_d_vol = models.DateField()
    date_f_vol = models.DateField()
    prix_vol = models.DecimalField(max_digits=15, decimal_places=2)
    def __str__(self):
        return f"{self.id_vol}"
class Utilisateur(models.Model):
    id_utilisateur = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=15)
    prenom = models.CharField(max_length=15)
    est_admin = models.BooleanField()
    mot_d_passe = models.CharField(max_length=10)
    num_telephone = models.CharField(max_length=12)
    email = models.EmailField()
    path_img_profile = models.CharField(max_length=100)
    id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"{self.nom} {self.prenom}"
    
class Voyage(models.Model):
    id_voyage = models.AutoField(primary_key=True)
    titre_voyage = models.CharField(max_length = 50)
    prix_voyage = models.DecimalField(max_digits=15, decimal_places=2)
    duree_voyage = models.IntegerField()
    transport = models.BooleanField()
    id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    id_promotion = models.ForeignKey(Promotion,on_delete=models.CASCADE,null=True)
    id_categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    def __str__(self):
        return self.titre_voyage
class Commentaire(models.Model):
    id_comment = models.AutoField(primary_key=True)
    text_comment = models.CharField(max_length=150)
    date_redaction = models.DateField()
    heure_redaction = models.TimeField()
    evaluation = models.IntegerField()
    id_voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    def __str__(self):
        return self.text_comment

class Recevoir(models.Model):
    id_utilisateur_1 = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    id_notification = models.ForeignKey(Notification, on_delete=models.CASCADE)

class ReserverVoyage(models.Model):
    id_utilisateur_1 = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    id_voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)

class Avoir(models.Model):
    id_voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    id_ville = models.ForeignKey(Ville, on_delete=models.CASCADE)

class Aimer(models.Model):
    id_utilisateur_1 = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    id_voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)

class inclure(models.Model):
    id_voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    id_vol = models.ForeignKey(Vol, on_delete=models.CASCADE)

