# Generated by Django 3.1.7 on 2021-04-08 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimes', '0004_crime_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crime',
            name='color',
        ),
        migrations.AlterField(
            model_name='crime',
            name='crime_type',
            field=models.CharField(choices=[('theft', 'Theft'), ('assault', 'Assault'), ('attempted murder', 'Attempted Murder'), ('robbery', 'Robbery'), ('peeping', 'Peeping')], default='theft', max_length=200),
        ),
    ]
