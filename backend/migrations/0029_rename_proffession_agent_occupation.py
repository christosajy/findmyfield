# Generated by Django 5.0.7 on 2024-08-11 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0028_rename_license_no_agent_proffession'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='proffession',
            new_name='occupation',
        ),
    ]
