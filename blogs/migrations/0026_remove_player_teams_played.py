# Generated by Django 3.2.7 on 2021-12-26 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0025_auto_20211226_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='teams_played',
        ),
    ]
