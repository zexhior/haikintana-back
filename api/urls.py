from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^membres/$', views.membre_list),
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
    url(r'^updates/(?P<pk>[0-9]+)$', views.update_membre),
    path('home', views.home, name='home')
]
