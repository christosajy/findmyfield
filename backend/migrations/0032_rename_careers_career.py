# Generated by Django 5.0.7 on 2024-08-24 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0031_rename_career_name_careers_career'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Careers',
            new_name='Career',
        ),
    ]
