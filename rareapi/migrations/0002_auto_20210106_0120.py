# Generated by Django 3.1.4 on 2021-01-06 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rareuser',
            name='profile_image',
            field=models.ImageField(default='', null=True, upload_to=''),
        ),
    ]
