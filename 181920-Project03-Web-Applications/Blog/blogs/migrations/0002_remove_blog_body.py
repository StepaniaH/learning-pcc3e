# Generated by Django 5.0.7 on 2024-08-11 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='body',
        ),
    ]
