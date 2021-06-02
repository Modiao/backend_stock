from django.db import models
from hidefield.fields import HideField
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from random_id.utils import generate_random_string as id_generator

# Create your models here.

from backend_stock.utilities import get_price
class HideCharField(HideField, models.CharField):
    pass

class Customer(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    email = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=500)

class Ticket(models.Model):
    TYPE_TICKET = Choices(
        ("Consultation_medecine_general", _("Consultation Médecine Générale")),
        ("Consultation_gyneco",_("Consultation Gynéco")),
        ("Consultation_pediatrique",_("Consultation Pédiatrique")),
        ("Consultation_sage_femme",_("Consultation Sage Femme")),
        ("Consultation_rhumatologie",_("Consultation Rhumatologie")),
        ("Consultation_cardiologie", _("Consultation Cardiologie")),
        ("Consultation_orl",_("Consultation ORL")),
        ("Consultation_orphtalologie", _("Consultation Ophtalmologie")),
        ("Hospitalisation_categorie_1",_("Hospitalisation Catégorie 1")),
        ("Hospitalisation_categorie_2", _("Hospitalisation Catégorie 2")),
        ("Hospitalisation_categorie_3", _("Hospitalisation Catégorie 3"))
    )

    id_ticket = models.CharField(
        'Refrence Ticket', max_length=11,
        editable=False, unique=True, primary_key=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    type = models.CharField(choices=TYPE_TICKET,
        default=TYPE_TICKET.Consultation_medecine_general, max_length=100)
    montant = models.IntegerField(editable=False)
    nom_patient = models.CharField(max_length=200)
    penom_patient = models.CharField(max_length=200)
    patient = HideCharField(max_length=500, editable=False)
    is_valid = models.BooleanField(default=True)

    def save(self):
        self.patient = self.penom_patient +" "+self.nom_patient
        self.montant = get_price.get(self.type)
        if not self.id_ticket:
            # Generate ID once, then the database. If exist, keep trying
            self.id_ticket = id_generator()
            print(self.id_ticket)
            while Ticket.objects.filter(id_ticket=self.id_ticket).exists():
                self.id_ticket = id_generator()
        super(Ticket, self).save()            
