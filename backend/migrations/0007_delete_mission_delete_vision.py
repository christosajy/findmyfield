# Generated by Django 5.0.7 on 2024-08-02 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_delete_aboutus_rename_point_1_mission_mission_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mission',
        ),
        migrations.DeleteModel(
            name='Vision',
        ),
    ]
