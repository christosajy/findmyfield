# Generated by Django 5.0.7 on 2024-08-05 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_rename_type_ground_ground_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='ground',
            name='locality',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='ground',
            name='map_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
