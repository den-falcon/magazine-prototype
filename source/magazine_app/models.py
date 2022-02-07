from django.db import models
from django.urls import reverse

from magazine_app.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Наименование')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    category = models.ForeignKey('magazine_app.Category', default=1, related_name='products', on_delete=models.CASCADE,
                                 verbose_name='Категория')
    remainder = models.IntegerField(null=True, blank=True, verbose_name='Остаток', validators=[MinValueValidator(0), ])
    price = models.DecimalField(max_length=10, max_digits=9, decimal_places=2, null=False, blank=False,
                                verbose_name='Стоимость', validators=[MinValueValidator(0.01), ])

    @staticmethod
    def get_absolute_url():
        return reverse('index')

    def __str__(self):
        return f'{self.name} | {self.category}'

    class Meta:
        db_table = 'magazine_app_product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'magazine_app_category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
