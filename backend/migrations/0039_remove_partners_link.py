# Generated by Django 5.0.7 on 2024-08-27 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0038_partners'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partners',
            name='link',
        ),
    ]
