# Generated by Django 5.0.7 on 2024-08-25 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0035_rename_career_career_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='closing_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='posted_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
