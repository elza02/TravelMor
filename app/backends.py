# backends.py

from django.contrib.auth.backends import ModelBackend
from django.contrib.sessions.models import Session
from .models import Utilisateur

class EmailMotDePasseBackend(ModelBackend):
    def authenticate(self, request, email=None, mot_de_passe=None, **kwargs):
        print("Custom Backend: authenticate called")
        try:
            user = Utilisateur.objects.get(email=email)
        except Utilisateur.DoesNotExist:
            return None

        if user.check_password(mot_de_passe):
            return user
        return None

    def get_user(self, user_id):
        print("Custom Backend: get_user called")
        try:
            return Utilisateur.objects.get(pk=user_id)
        except Utilisateur.DoesNotExist:
            return None
