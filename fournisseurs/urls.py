from django.conf.urls import include, url

from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.indexFournisseurs, name='indexF'),
	url(r'^fournisseurs/', views.detail, name='detail'),
]
