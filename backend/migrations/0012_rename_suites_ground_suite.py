# Generated by Django 5.0.7 on 2024-08-04 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_rename_image_ground_image_1_ground_image_2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ground',
            old_name='suites',
            new_name='suite',
        ),
    ]
