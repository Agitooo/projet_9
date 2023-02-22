from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Ticket(models.Model):
    photo = models.ImageField(null=True)
    titre = models.CharField(max_length=128)
    contenu = models.CharField(max_length=5000)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True, editable=True)
    objects = models.Manager()


class Review(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    titre = models.CharField(max_length=128)
    vote = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    contenu = models.CharField(max_length=5000)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True, editable=True)
    objects = models.Manager()
