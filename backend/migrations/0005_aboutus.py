# Generated by Django 5.0.7 on 2024-08-02 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_mission_vision'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission', models.TextField(blank=True, null=True)),
                ('vision', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
