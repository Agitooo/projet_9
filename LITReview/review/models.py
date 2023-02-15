from django.conf import settings
from django.db import models


class Ticket(models.Model):
    photo = models.ImageField(null=True)
    titre = models.CharField(max_length=128)
    contenu = models.CharField(max_length=5000)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
