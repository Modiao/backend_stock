# Generated by Django 3.2.3 on 2021-05-31 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_ticket_id_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='id_ticket',
            field=models.CharField(editable=False, max_length=11, primary_key=True, serialize=False, unique=True, verbose_name='Refrence Ticket'),
        ),
    ]