from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from jarvis import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',  views.home, name="home"),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^produits/', include('produit.urls')),
    url(r'^fournisseurs/', include('fournisseurs.urls')),
    url(r'^panier/', include('panier.urls')),
    url(r'^users/', include('register.urls')),
]