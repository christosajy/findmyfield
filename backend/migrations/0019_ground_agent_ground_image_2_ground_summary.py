# Generated by Django 5.0.7 on 2024-08-06 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_remove_ground_agent_remove_ground_ground_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ground',
            name='agent',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='ground',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='stadium'),
        ),
        migrations.AddField(
            model_name='ground',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
