# Generated by Django 5.0.7 on 2024-08-28 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0042_rename_id_no_agent_whatsapp_remove_agent_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='whatsapp',
            new_name='applicant',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='image',
        ),
    ]
