# Generated by Django 5.1 on 2024-08-28 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_projectphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectphoto',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.projects', verbose_name='Проект'),
        ),
    ]
