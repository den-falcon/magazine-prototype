# Generated by Django 4.0.1 on 2022-01-12 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание')),
                ('category', models.CharField(choices=[('other', 'Прочее'), ('clothes', 'Одежда'), ('electronics', 'Электронника'), ('for_home', 'Для дома'), ('accessories', 'Аксессуары')], default='other', max_length=100, verbose_name='Категория')),
                ('remainder', models.IntegerField(blank=True, null=True, verbose_name='Остаток')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, max_length=10, verbose_name='Стоимость')),
            ],
        ),
    ]
