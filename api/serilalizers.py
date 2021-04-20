from rest_framework import serializers
from .models import *

class MembreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membre
        fields = ('id',
                  'nom',
                  'prenom',
                  'adr_phys',
                  'date_add',
                  'cotisation',
                  'nbr_paiement',
                  #'photo',)
                  'linkedin',
                  'statut',
                  'nummembre',
                  'fbmembre',
                  'mailmembre'
                  )

class NumeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactNum
        fields = ('numero', 'membre',)

class FbSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactFb
        fields = ('nom_compte', 'membre',)

class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMail
        fields = ('adr_mail', 'membre',)

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ('type', 'activities',)

class ActiviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activite
        fields = ('theme', 'date', 'categorie', 'photos')

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('url_image', 'activite')

class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ('paragraphe', 'activite')

class PresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presence
        fields = ('presence', 'activite', 'membre')