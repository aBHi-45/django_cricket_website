# Generated by Django 3.2.7 on 2021-12-26 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0024_match_toss_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='BBI',
            field=models.CharField(default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='player',
            name='BBM',
            field=models.CharField(default='-', max_length=40),
        ),
    ]
