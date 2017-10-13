from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.indexProduit, name='indexProduit'),
    url(r'^(?P<id>[0-9]+)/$', views.detailProduit, name='detailProduit'),
]
