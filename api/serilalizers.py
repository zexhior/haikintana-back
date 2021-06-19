from rest_framework import serializers
from django import forms
from .models import *

class MembreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membre
        fields = ('id',
                  'nom',
                  'prenom',
                  'adr_phys',
                  'date_add',
                  'linkedin',
                  'statut',
                  'nummembre',
                  'fbmembre',
                  'mailmembre',
                  'photoprofil',
                  'presencemembre',
                  )

class MembreSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membre
        fields = ('id',
                  'nom',
                  'prenom',
                  'adr_phys',
                  'date_add',
                  'linkedin',
                  'statut',
                  #'nummembre',
                  #'fbmembre',
                  #'mailmembre',
                  #photoprofil',
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
        fields = ('id','type',)

class ActiviteSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activite
        fields = ('id',
                  'theme',
                  'date',
                  'categorie',
                  #'descriptions',
                  #'photos'
                 )

class ActiviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activite
        fields = ('id',
                  'theme',
                  'date',
                  'categorie',
                  'descriptions',
                  'photos',
                 )

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

class ContactOrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactOrganisation
        fields = ('email', 'numero', 'bancaire', 'facebook')

class CotisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotisation
        fields = ('motif', 'montant', 'activite')

class PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        fields = ('montant', 'ref', 'membre', 'cotisation')

class PhotoProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoProfil
        fields = ('id','photo', 'membre',)

class RegleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regle
        fields = ('numero', 'description', 'activite')

class PhotoProfilForm(forms.ModelForm):
    class Meta:
        model = PhotoProfil
        fields = ('photo', 'membre',)