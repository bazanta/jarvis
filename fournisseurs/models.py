# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Fournisseur(models.Model):
   nom = models.CharField(max_length=30)
   adresse1 = models.CharField(max_length=100)
   adresse2 = models.CharField(max_length=100)

   def __str__(self):
       return self.nom
