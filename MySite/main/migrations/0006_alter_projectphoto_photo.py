# Generated by Django 5.1 on 2024-08-31 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_projectphoto_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectphoto',
            name='photo',
            field=models.ImageField(upload_to='media/media/project_photo', verbose_name='Фото'),
        ),
    ]