# Generated by Django 4.2 on 2023-07-15 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='films',
            field=models.ManyToManyField(related_name='films', to='API.film'),
        ),
    ]
