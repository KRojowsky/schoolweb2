# Generated by Django 3.2.19 on 2023-06-28 08:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20230628_0844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='likes',
        ),
        migrations.AddField(
            model_name='room',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_rooms', to=settings.AUTH_USER_MODEL),
        ),
    ]