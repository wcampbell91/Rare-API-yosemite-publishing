# Generated by Django 3.1.3 on 2020-12-08 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0002_auto_20201208_0132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='label',
        ),
    ]
