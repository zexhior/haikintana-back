from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^membres/$', views.membre_list),
    path('home', views.home, name='home')
]
