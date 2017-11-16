from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from . import views
from .flux import DerniersCommentairesFeed

urlpatterns = [
    url(r'^$', views.indexProduit, name='indexProduit'),
    url(r'^addCommentaire/(?P<id>[0-9]+)$', views.addCommentaire, name="addCommentaire"),
    url(r'^add/(?P<id>[0-9]+)$', views.addProductPanier, name="addProductPanier"),
    url(r'^(?P<id>[0-9]+)/$', views.detailProduit, name='detailProduit'),
    url(r'^rss$', DerniersCommentairesFeed())
]