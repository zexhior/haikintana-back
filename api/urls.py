from django.urls import path
from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

route = DefaultRouter()
route.register('membrecreation',views.MembreCreation)
route.register('photocreation',views.PhotoCreation)

urlpatterns = [
    path('',include(route.urls)),

    url(r'^membres/$', views.membre_list),
    url(r'^membres/(?P<pk>[0-9]+)$', views.membre_get_update_delete),

    url(r'^numeros/$', views.numero_list),
    url(r'^numeros/(?P<pk>[0-9]+)$', views.numero_get_update_delete),

    url(r'^fbs/$', views.fb_list),
    url(r'^fbs/(?P<pk>[0-9]+)$', views.fb_get_update_delete),

    url(r'^mails/$', views.mail_list),
    url(r'^mails/(?P<pk>[0-9]+)$', views.mail_get_update_delete),

    url(r'^categories/$', views.categorie_list),
    url(r'^categories/(?P<pk>[0-9]+)$', views.categorie_get_update_delete),

    url(r'^activites/$', views.activite_list),
    url(r'^activites/(?P<pk>[0-9]+)$', views.activite_get_update_delete),

    url(r'^descriptions/$', views.description_list),
    url(r'^descriptions/(?P<pk>[0-9]+)$', views.description_get_update_delete),

    url(r'^photos/$', views.photo_list),
    url(r'^photos/(?P<pk>[0-9]+)$', views.photo_get_update_delete),

    url(r'^presences/$', views.presence_list),
    url(r'^presences/(?P<pk>[0-9]+)$', views.presence_get_update_delete),

    url(r'^contactorganisations/$', views.contact_organisation_list),
    url(r'^contactorganisations/(?P<pk>[0-9]+)$', views.contact_organisation_get_update_delete),

    url(r'^cotisations/$', views.cotisation_list),
    url(r'^cotisations/(?P<pk>[0-9]+)$', views.cotisation_get_update_delete),

    url(r'^paiements/$', views.paiement_list),
    url(r'^paiements/(?P<pk>[0-9]+)$', views.paiement_get_update_delete),

    url(r'^photoprofils/$', views.photoprofil_list),
    url(r'^photoprofils/(?P<pk>[0-9]+)$', views.photoprofil_get_update_delete),

    url(r'^regles/$', views.regle_list),
    url(r'^regles/(?P<pk>[0-9]+)$', views.regle_get_update_delete),

    url(r'^updates/(?P<pk>[0-9]+)$', views.update_membre),
    url(r'^$', views.home, name='home'),
    url(r'^qrcode/$', views.testCodeQr),
]