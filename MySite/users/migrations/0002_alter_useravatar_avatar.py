# Generated by Django 5.1 on 2024-09-01 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useravatar',
            name='avatar',
            field=models.ImageField(default='media/media/UserAvatars/', upload_to='media/UserAvatars', verbose_name='Аватар'),
        ),
    ]