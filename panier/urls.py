from django.conf.urls import url, include
from django.contrib import admin

from panier import views

urlpatterns = [
    url(r'^$', views.panier, name="panier"),
]
