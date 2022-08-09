# Generated by Django 4.1 on 2022-08-08 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=500)),
                ('autor', models.CharField(max_length=50)),
                ('creation_date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]