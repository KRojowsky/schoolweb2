# Generated by Django 3.2.19 on 2023-08-15 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_auto_20230815_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='event_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]