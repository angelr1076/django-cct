# Generated by Django 3.1 on 2021-06-25 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suspects', '0011_alter_suspect_spotted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suspect',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
