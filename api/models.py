from django.db import models

#membre
class Membre(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adr_phys = models.CharField(max_length=100)
    date_add = models.DateField(auto_now_add=True)
    linkedin = models.CharField(max_length=100)
    statut = models.CharField(max_length=100)

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

    def __str__(self):
        return "{}".format(self.type)

class Activite(models.Model):
    theme = models.CharField(max_length=200, null=False)
    date = models.DateField(null=False)
    categorie = models.ForeignKey(Categorie, default=1, related_name='activities', on_delete=models.CASCADE)

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
    activite = models.ForeignKey(Activite, related_name='presences', on_delete= models.CASCADE)
    membre = models.ForeignKey(Membre, related_name='presencemembre', on_delete= models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.presence)

#ContactOrganisation
class ContactOrganisation(models.Model):
    email = models.CharField(max_length=150, default="", null=True)
    numero = models.CharField(max_length=20)
    bancaire = models.CharField(max_length=25)
    facebook = models.CharField(max_length=100)

class Regle(models.Model):
    numero = models.SmallIntegerField(default=0)
    description = models.CharField(default="", max_length=150, null=False)
    activite = models.ForeignKey(Activite, related_name='regles', on_delete= models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.numero, self.description)

class Cotisation(models.Model):
    motif= models.CharField(default="",max_length=300,null=False)
    montant = models.BigIntegerField(default=0, null=False)
    activite = models.ForeignKey(Activite, related_name='activite', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{} {} {}".format(self.membre, self.montant, self.ref)

class PhotoProfil(models.Model):
    photo = models.ImageField(upload_to='images')
    membre = models.OneToOneField(Membre, related_name='photoprofil', on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.photo, self.membre)

class Paiement(models.Model):
    montant = models.BigIntegerField(null=False)
    ref = models.CharField(max_length=100,null=False)
    membre = models.ForeignKey(Membre, related_name='paiementmembre', on_delete=models.CASCADE)
    cotisation = models.ForeignKey(Cotisation, related_name="paiementcotisation", on_delete=models.CASCADE)

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