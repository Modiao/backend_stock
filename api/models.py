from django.db import models
from hidefield.fields import HideField

# Create your models here.


class HideCharField(HideField, models.CharField):
    pass

class Customer(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    email = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=500)

class Tickets(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=500)
    montant = models.IntegerField()
    nom_patient = models.CharField(max_length=200)
    penom_patient = models.CharField(max_length=200)
    patient = HideCharField(max_length=500)

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.patient = self.penom_patient +" "+self.nom_patient
        
