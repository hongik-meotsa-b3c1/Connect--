# Generated by Django 3.0.14 on 2022-03-06 09:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20220306_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviepost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviepost',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
