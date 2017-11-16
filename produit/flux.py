from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Commentaire

class DerniersCommentairesFeed(Feed):
    title = "Commentaires"
    link = "/commentaires/"
    description = "Voici les derniers commentaires"

    def items(self):
        return Commentaire.objects.order_by('-date')[:3]

    def item_title(self, item):
        return item.auteur

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return reverse('detailProduit', args=[item.produit.pk])