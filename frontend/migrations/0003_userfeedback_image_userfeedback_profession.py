# Generated by Django 5.0.7 on 2024-08-10 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_rename_feed_userfeedback_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfeedback',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='feeds'),
        ),
        migrations.AddField(
            model_name='userfeedback',
            name='profession',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
