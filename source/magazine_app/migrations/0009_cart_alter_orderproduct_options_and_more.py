# Generated by Django 4.0.1 on 2022-02-28 21:57

from django.db import migrations, models
import django.db.models.deletion
import magazine_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('magazine_app', '0008_order_orderproduct_order_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(validators=[magazine_app.validators.MinValueValidator(1)], verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Товар в корзине',
                'verbose_name_plural': 'Товары в корзине',
                'db_table': 'magazine_app_cart',
            },
        ),
        migrations.AlterModelOptions(
            name='orderproduct',
            options={'verbose_name': 'Товар в заказе', 'verbose_name_plural': 'Товары в заказе'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.RenameField(
            model_name='orderproduct',
            old_name='count',
            new_name='qty',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='remainder',
            new_name='amount',
        ),
        migrations.AlterModelTable(
            name='orderproduct',
            table=None,
        ),
        migrations.DeleteModel(
            name='ProductInCart',
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='magazine_app.product', verbose_name='Товары в корзине'),
        ),
    ]
