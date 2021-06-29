from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class StatutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statut
        fields = ('id', 'poste')

class PresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presence
        fields = ('id', 'presence', 'activite', 'membre')

class PhotoProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoProfil
        fields = ('id','photo', 'membre',)

class NumeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactNum
        fields = ('id', 'numero', 'membre',)

class FbSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactFb
        fields = ('id', 'nom_compte', 'membre',)

class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMail
        fields = ('id', 'adr_mail', 'membre',)

class MembreSerializer(serializers.ModelSerializer):
    statut = StatutSerializer()
    fbmembre = FbSerializer(many=True)
    nummembre = NumeroSerializer(many=True)
    mailmembre = MailSerializer(many=True)
    photoprofil = PhotoProfilSerializer(many=False)
    presencemembre = PresenceSerializer(many=True)

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
                  'mdp',
                  #'nummembre',
                  #'fbmembre',
                  #'mailmembre',
                  #photoprofil',
                  )

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'image', 'url_image', 'description')

class DescriptionSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Description
        fields = ('id', 'titre', 'paragraphe', 'activite')

class DescriptionSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Description
        fields = ('id', 'titre', 'paragraphe', 'activite','photos',)

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ('id','type')

class ActiviteSaveSerializer(serializers.ModelSerializer):
    #categorie = CategorieSerializer();

    class Meta:
        model = Activite
        fields = ('id',
                  'theme',
                  'date',
                  'categorie',
                 )

class ActiviteSerializer(serializers.ModelSerializer):
    descriptions = DescriptionSerializer(many=True)
    categorie = CategorieSerializer();

    class Meta:
        model = Activite
        fields = ('id',
                  'theme',
                  'date',
                  'categorie',
                  'descriptions',
                 )

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

class RegleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regle
        fields = ('numero', 'description', 'activite')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')