# Generated by Django 5.1 on 2024-10-18 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='media/user_avatars', verbose_name='Аватар'),
        ),
    ]
