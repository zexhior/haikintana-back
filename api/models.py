from django.db import models

class Association(models.Model):
    nom = models.CharField(max_length=100,null=False)
    localisation = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images')

#ContactOrganisation
class ContactOrganisation(models.Model):
    email = models.CharField(max_length=150, default="", null=True)
    numero = models.CharField(max_length=20)
    bancaire = models.CharField(max_length=25)
    facebook = models.CharField(max_length=100)
    association = models.ForeignKey(Association, default=1, related_name="contactorganisations", on_delete=models.CASCADE)

#membre
class Membre(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adr_phys = models.CharField(max_length=100)
    date_add = models.DateField(auto_now_add=True)
    nbr_paiement = models.SmallIntegerField()
    photo = models.ImageField(upload_to='images')
    linkedin = models.CharField(max_length=100)
    statut = models.CharField(max_length=100)
    association = models.ForeignKey(Association, default=1,  related_name="association_membres", on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.nom, self.prenom)

class ContactNum(models.Model):
    numero = models.CharField(max_length=10, null=False, unique=True)
    membre = models.ForeignKey(Membre, related_name='nummembre', on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.numero)

class ContactFb(models.Model):
    nom_compte= models.CharField(max_length=200, null=False, unique= True)
    membre = models.ForeignKey(Membre, related_name='fbmembre', on_delete= models.CASCADE)

    def __str__(self):
        return "{}".format(self.nom_compte)

class ContactMail(models.Model):
    adr_mail = models.EmailField(max_length=100, null=False, unique=True)
    membre = models.ForeignKey(Membre, related_name='mailmembre', on_delete= models.CASCADE)

    def __str__(self):
        return "{}".format(self.adr_mail)

class Categorie(models.Model):
    type = models.CharField(max_length=100, null=False)
    association = models.ForeignKey(Association, default=1,  related_name="association_categories", on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.type)

class Activite(models.Model):
    theme = models.CharField(max_length=200, null=False)
    date = models.DateField(null=False)
    association = models.ForeignKey(Association, default=1,  related_name="association_activites", on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, related_name='activities' ,on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.theme)

class Photo(models.Model):
    url_image = models.ImageField(upload_to='images')
    activite = models.ForeignKey(Activite, related_name='photos', on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.url_image)

class Description(models.Model):
    paragraphe = models.CharField(max_length=1000, null=False)
    activite = models.ForeignKey(Activite, related_name='descriptions', on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.paragraphe)

class Presence(models.Model):
    presence = models.BooleanField(default=False)
    contrepresence = models.BooleanField(default=False)
    activite = models.ForeignKey(Activite, related_name='activites', on_delete= models.CASCADE)
    membre = models.ForeignKey(Membre, related_name='membres', on_delete= models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.presence)

class Regle(models.Model):
    numero = models.SmallIntegerField(default=0)
    description = models.CharField(default="", max_length=150, null=False)
    activite = models.ForeignKey(Activite, related_name='regles', on_delete= models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.numero, self.description)

class Cotisation(models.Model):
    montant = models.BigIntegerField(default=0)
    ref = models.CharField(max_length=30, null=False)
    membre = models.ForeignKey(Membre, related_name="cotisations", null=False, on_delete= models.CASCADE)

    def __str__(self):
        return "{} {} {}".format(self.membre, self.montant, self.ref)

#{
#    'nom' = "RAKOTO",
#    'prenom' = "Rabe",
#    'adr_phys' = "Lot II Q 20 Analamahintsy",
#    'cotisation' = 25000,
#    'nbr_paiemen't = 1,
#    'photo' = "https://www.haikitana.com/sary.png",
#    'lindekin' = "RAKOTO Rabe",
#    'statut' = "adherent"
#}