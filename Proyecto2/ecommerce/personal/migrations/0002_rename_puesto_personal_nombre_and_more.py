# Generated by Django 4.1 on 2022-08-09 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personal',
            old_name='Puesto',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='personal',
            old_name='name',
            new_name='puesto',
        ),
    ]
