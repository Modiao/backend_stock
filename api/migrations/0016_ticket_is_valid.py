# Generated by Django 3.2.3 on 2021-06-02 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_ticket_montant'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='is_valid',
            field=models.BooleanField(default=True),
        ),
    ]