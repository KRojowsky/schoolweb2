# Generated by Django 3.2.19 on 2023-08-14 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_roommember'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommember',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.post'),
        ),
    ]