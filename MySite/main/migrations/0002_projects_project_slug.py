# Generated by Django 5.1 on 2024-08-28 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='project_slug',
            field=models.SlugField(default='dbhsjhfd', max_length=255, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
    ]