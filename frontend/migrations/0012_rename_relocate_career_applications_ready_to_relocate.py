# Generated by Django 5.0.7 on 2024-08-25 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0011_career_applications'),
    ]

    operations = [
        migrations.RenameField(
            model_name='career_applications',
            old_name='relocate',
            new_name='ready_to_relocate',
        ),
    ]
