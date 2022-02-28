# Generated by Django 4.0.1 on 2022-02-08 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magazine_app', '0007_alter_productincart_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Имя пользователя')),
                ('phone', models.CharField(max_length=15, verbose_name='Телефон')),
                ('address', models.CharField(max_length=100, verbose_name='Адресс')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'db_table': 'magazine_app_order',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_in_order', to='magazine_app.order', verbose_name='Товары в заказе')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_in_order', to='magazine_app.product', verbose_name='Товары в заказе')),
            ],
            options={
                'verbose_name': 'Количество в заказе',
                'verbose_name_plural': 'Количество в заказах',
                'db_table': 'magazine_app_order_product',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='orders', through='magazine_app.OrderProduct', to='magazine_app.Product'),
        ),
    ]