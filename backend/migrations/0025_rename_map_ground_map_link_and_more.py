# Generated by Django 5.0.7 on 2024-08-08 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0024_rename_summary_agent_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ground',
            old_name='map',
            new_name='map_link',
        ),
        migrations.RenameField(
            model_name='ground',
            old_name='web',
            new_name='web_link',
        ),
    ]
