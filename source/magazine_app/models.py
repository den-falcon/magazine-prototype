from django.db import models
from django.urls import reverse
from django.db.models import F, ExpressionWrapper as E, Sum

from magazine_app.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Наименование')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    category = models.ForeignKey('magazine_app.Category', default=1, related_name='products', on_delete=models.CASCADE,
                                 verbose_name='Категория')
    amount = models.IntegerField(null=True, blank=True, verbose_name='Остаток', validators=[MinValueValidator(0), ])
    price = models.DecimalField(max_length=10, max_digits=9, decimal_places=2, null=False, blank=False,
                                verbose_name='Стоимость', validators=[MinValueValidator(0.01), ])

    @staticmethod
    def get_absolute_url():
        return reverse('index')

    def __str__(self):
        return f'{self.name} | {self.category}'

    class Meta:
        db_table = 'magazine_app_product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'magazine_app_category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Cart(models.Model):
    product = models.ForeignKey('magazine_app.Product', related_name='cart', on_delete=models.CASCADE,
                                verbose_name='Товары в корзине')
    qty = models.IntegerField(verbose_name='Количество', validators=[MinValueValidator(1), ])

    def __str__(self):
        return f'{self.product.name} - {self.qty}'

    # def get_product_total(self):
    #     return self.qty * self.product.price

    @classmethod
    def get_with_total(cls):
        return cls.objects.annotate(total=E(F("qty") * F("product__price"), output_field=models.DecimalField()))

    @classmethod
    def get_with_product(cls):
        return cls.get_with_total().select_related("product")

    @classmethod
    def get_cart_total(cls):
        total = cls.get_with_total().aggregate(cart_total=Sum("total"))
        return total['cart_total']

    class Meta:
        db_table = 'magazine_app_cart'
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'


class Order(models.Model):
    products = models.ManyToManyField('magazine_app.Product', related_name='orders', through='magazine_app.OrderProduct',
                                      through_fields=('order', 'product'))
    name = models.CharField(max_length=40, verbose_name='Имя пользователя')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    address = models.CharField(max_length=100, verbose_name='Адресс')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.products} | {self.name}'

    class Meta:
        db_table = 'magazine_app_order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderProduct(models.Model):
    product = models.ForeignKey('magazine_app.Product', related_name='products_in_order', on_delete=models.CASCADE,
                                verbose_name='Товары в заказе')
    order = models.ForeignKey('magazine_app.Order', related_name='orders_in_order', on_delete=models.CASCADE,
                              verbose_name='Товары в заказе')
    qty = models.PositiveIntegerField(verbose_name='Количество')

    def __str__(self):
        return f'{self.product.name} - {self.order.name}'

    class Meta:
        db_table = 'magazine_app_orderproduct'
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'


