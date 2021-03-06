# Generated by Django 3.2 on 2021-05-31 13:50

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210531_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.role', verbose_name='Роль'),
        ),
        migrations.CreateModel(
            name='receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Телефон')),
                ('address', models.CharField(max_length=50, verbose_name='Адрес')),
                ('sum_cost', models.DecimalField(decimal_places=2, max_digits=20, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Сумма заказа')),
                ('delivery_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.delivery_type', verbose_name='Тип доставки')),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.receipt_status', verbose_name='Статус')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='massage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500, verbose_name='Текст')),
                ('receipt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.receipt', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='receipt_has_product',
            fields=[
                ('receipt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.receipt', verbose_name='Заказ')),
                ('price', models.DecimalField(decimal_places=2, max_digits=40, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Цена')),
                ('amount', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(Decimal('1'))], verbose_name='Количество')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Заказ-продукт',
                'verbose_name_plural': 'Заказы-продукты',
                'unique_together': {('receipt_id', 'product_id')},
            },
        ),
    ]
