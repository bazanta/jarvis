# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Fournisseur(models.Model):
   nom = models.CharField(max_length=30)
   # Localisation
   adresse1 = models.CharField(max_length=100)
   adresse2 = models.CharField(max_length=100, blank=True)
   codePostal = models.CharField(max_length=5, default="49000")
   ville = models.CharField(max_length=80, default="Angers")

   def __str__(self):
       return self.nom
