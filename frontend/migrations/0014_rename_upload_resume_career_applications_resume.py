# Generated by Django 5.0.7 on 2024-08-25 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0013_rename_resume_career_applications_upload_resume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='career_applications',
            old_name='upload_resume',
            new_name='resume',
        ),
    ]
