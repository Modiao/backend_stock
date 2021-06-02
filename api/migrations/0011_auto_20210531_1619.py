# Generated by Django 3.2.3 on 2021-05-31 16:19

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_ticket_id_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='id_ticket',
            field=models.CharField(editable=False, max_length=11, null=True, unique=True, verbose_name='Refrence Ticket'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='patient',
            field=api.models.HideCharField(editable=False, max_length=500),
        ),
    ]