# Generated by Django 5.0 on 2024-01-14 00:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_hotel_petit_dejeuner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='id_hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.hotel'),
        ),
    ]
