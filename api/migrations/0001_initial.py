# Generated by Django 3.2.3 on 2021-06-03 10:55

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=20)),
                ('email', models.CharField(blank=True, max_length=500, null=True)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id_ticket', models.CharField(editable=False, max_length=11, primary_key=True, serialize=False, unique=True, verbose_name='Refrence Ticket')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('Consultation_medecine_general', 'Consultation Médecine Générale'), ('Consultation_gyneco', 'Consultation Gynéco'), ('Consultation_pediatrique', 'Consultation Pédiatrique'), ('Consultation_sage_femme', 'Consultation Sage Femme'), ('Consultation_rhumatologie', 'Consultation Rhumatologie'), ('Consultation_cardiologie', 'Consultation Cardiologie'), ('Consultation_orl', 'Consultation ORL'), ('Consultation_orphtalologie', 'Consultation Ophtalmologie'), ('Hospitalisation_categorie_1', 'Hospitalisation Catégorie 1'), ('Hospitalisation_categorie_2', 'Hospitalisation Catégorie 2'), ('Hospitalisation_categorie_3', 'Hospitalisation Catégorie 3')], default='Consultation_medecine_general', max_length=100)),
                ('montant', models.IntegerField(editable=False)),
                ('nom_patient', models.CharField(max_length=200)),
                ('penom_patient', models.CharField(max_length=200)),
                ('patient', api.models.HideCharField(editable=False, max_length=500)),
                ('is_valid', models.BooleanField(default=True)),
            ],
        ),
    ]
