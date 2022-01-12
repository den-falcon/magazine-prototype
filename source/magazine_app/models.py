from django.db import models

CATEGORY_CHOICES = [('other', 'Прочее'), ('clothes', 'Одежда'), ('electronics', 'Электронника'),
                    ('for_home', 'Для дома'), ('accessories', 'Аксессуары')]


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Наименование')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='other', verbose_name='Категория')
    remainder = models.IntegerField(null=True, blank=True, verbose_name='Остаток')
    price = models.DecimalField(max_length=10, max_digits=9, decimal_places=2, null=False, blank=False,
                                verbose_name='Стоимость')
