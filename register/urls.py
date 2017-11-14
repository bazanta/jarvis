from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^signup$', views.signup, name='signup'),
    url(r'^connexion/', include('django.contrib.auth.urls')),
]