# Generated by Django 5.0.7 on 2024-08-24 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0030_careers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='careers',
            old_name='career_name',
            new_name='career',
        ),
    ]
