from django.conf.urls import url, include
from django.contrib import admin

from jarvis import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',  views.home, name="home"),
    url(r'^produits/', include('produit.urls')),
]
