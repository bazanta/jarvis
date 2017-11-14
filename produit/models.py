from django.db import models
from django.conf import settings
from django.utils import timezone

class FicheProduit(models.Model):
    nom = models.CharField(max_length=30)
    reference = models.CharField(max_length=45)
    descCourte = models.CharField(max_length=100)
    descLong = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=19, decimal_places=9)
    stock = models.IntegerField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nom

class Commentaire(models.Model):
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    produit = models.ForeignKey(FicheProduit, related_name="commentaires")
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text