from django.conf.urls import url, include
from django.contrib import admin

from panier import views

urlpatterns = [
    url(r'^$', views.panier, name="panier"),
    url(r'^delete/(?P<id>[0-9]+)$', views.panierSup, name="panierSup"),
    url(r'^modif/(?P<id>[0-9]+)$', views.panierModif, name="panierModif")
]
