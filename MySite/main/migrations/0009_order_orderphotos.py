# Generated by Django 5.1 on 2024-09-01 21:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_projectphoto_photo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=250, verbose_name='Тема')),
                ('email', models.EmailField(max_length=100, verbose_name='Электронная почта')),
                ('phone_number', models.IntegerField(verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=300, verbose_name='Адрес доставки')),
                ('description', models.TextField(verbose_name='Описание заказа')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заказы',
                'verbose_name_plural': 'Заказ',
            },
        ),
        migrations.CreateModel(
            name='OrderPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media/orderPhotos', verbose_name='Фото')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фото',
            },
        ),
    ]
