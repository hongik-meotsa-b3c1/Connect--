# Generated by Django 3.0.14 on 2022-03-02 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20220301_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieinfo',
            name='movie_actor',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='moviepost',
            name='movie_actor',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='moviepost',
            name='movie_director',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
