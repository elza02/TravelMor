# Generated by Django 5.0.1 on 2024-02-06 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_reservervoyage_id_vol'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='wifi',
            field=models.BooleanField(default=False),
        ),
    ]
