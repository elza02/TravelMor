# Generated by Django 5.0.1 on 2024-01-23 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_id_utilisateur_1_aimer_id_utilisateur_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='path_image',
            field=models.CharField(max_length=50),
        ),
    ]
