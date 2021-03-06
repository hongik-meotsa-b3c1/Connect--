# Generated by Django 3.0.14 on 2022-02-25 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=30)),
                ('movie_image', models.CharField(max_length=30)),
                ('movie_link', models.CharField(max_length=30)),
                ('movie_director', models.CharField(max_length=30)),
                ('movie_pubDate', models.CharField(max_length=20)),
                ('movie_userRating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MoviePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=700)),
                ('movie_title', models.CharField(max_length=700)),
                ('movie_image', models.CharField(max_length=100)),
                ('movie_link', models.CharField(max_length=100)),
                ('NumOfPeople', models.IntegerField()),
                ('gather_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('USER_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
