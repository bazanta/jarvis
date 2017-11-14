from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.indexProduit, name='indexProduit'),
    url(r'^add/(?P<id>[0-9]+)$', views.addProductPanier, name="addProductPanier"),
    url(r'^(?P<id>[0-9]+)/$', views.detailProduit, name='detailProduit'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)