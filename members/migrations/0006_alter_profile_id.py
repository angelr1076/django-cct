# Generated by Django 4.1.7 on 2023-05-19 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20210625_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]