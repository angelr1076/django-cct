# Generated by Django 3.2 on 2021-04-26 11:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('suspects', '0009_auto_20210426_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suspect',
            name='likes',
        ),
        migrations.AddField(
            model_name='suspect',
            name='spotted',
            field=models.ManyToManyField(blank=True, related_name='spotted_suspect', to=settings.AUTH_USER_MODEL),
        ),
    ]
