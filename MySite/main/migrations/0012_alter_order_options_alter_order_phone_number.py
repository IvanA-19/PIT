# Generated by Django 5.1 on 2024-09-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_order_photo_delete_orderphotos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.TextField(verbose_name='Номер телефона'),
        ),
    ]
