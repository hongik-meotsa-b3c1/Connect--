# Generated by Django 3.0.14 on 2022-01-23 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20220123_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieinfo',
            name='movie_userRating',
            field=models.FloatField(),
        ),
    ]
