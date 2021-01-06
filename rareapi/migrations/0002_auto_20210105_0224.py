# Generated by Django 3.1.4 on 2021-01-05 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rareuser',
            name='profile_image',
        ),
        migrations.CreateModel(
            name='UserAvatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(null=True, upload_to='useravatars')),
                ('rare_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='avatars', to='rareapi.rareuser')),
            ],
        ),
    ]
