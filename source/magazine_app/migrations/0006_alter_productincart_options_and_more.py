# Generated by Django 4.0.1 on 2022-02-08 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine_app', '0005_alter_product_price_alter_product_remainder_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productincart',
            options={'verbose_name': 'Товар в корзине', 'verbose_name_plural': 'Товары в корзине'},
        ),
        migrations.AlterModelTable(
            name='productincart',
            table='magazine_app_product_in_cart',
        ),
    ]
