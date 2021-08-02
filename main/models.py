from decimal import Decimal
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class receipt_status(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'

    def __str__(self):
        return self.name


class delivery_type(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Тип доставки'
        verbose_name_plural = 'Типы доставок'

    def __str__(self):
        return self.name


class role(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)
    description = models.CharField('Описание', max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return self.name


class user(models.Model):
    login = models.CharField('Логин', max_length=20, unique=True)
    password = models.CharField('Пароль', max_length=20)
    name = models.CharField('Имя', max_length=20)
    phone = PhoneNumberField('Телефон', unique=True)
    address = models.CharField('Адрес', max_length=50)
    role_id = models.ForeignKey(role, on_delete=models.PROTECT, verbose_name='Роль')

    class Meta:
        verbose_name = 'Пользоваатель'
        verbose_name_plural = 'Пользоваатели'

    def __str__(self):
        return self.login


class receipt(models.Model):
    contact = PhoneNumberField('Телефон')
    address = models.CharField('Адрес', max_length=50, default='ул. XXXXXXXXXXXX, XX.')
    sum_cost = models.DecimalField('Сумма заказа', max_digits=20, decimal_places=2,
                                   validators=[MinValueValidator(Decimal('0.01'))])
    status_id = models.ForeignKey(receipt_status, on_delete=models.PROTECT, verbose_name='Статус')
    delivery_id = models.ForeignKey(delivery_type, on_delete=models.PROTECT, verbose_name='Тип доставки')
    user_id = models.ForeignKey(user, on_delete=models.SET_NULL, verbose_name='Пользователь', null=True, blank=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.address


class product_type(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товаров'

    def __str__(self):
        return self.name


class product(models.Model):
    name = models.CharField('Название', max_length=50)
    price = models.DecimalField('Цена', max_digits=20, decimal_places=2,
                                validators=[MinValueValidator(Decimal('0.01'))])
    amount = models.PositiveIntegerField('Количество')
    animal = models.CharField('Животное', max_length=50)
    img = models.ImageField('Изображение', upload_to='static/main/img',
                            default='static/main/img/standart_foto.png')
    product_type_id = models.ForeignKey(product_type, on_delete=models.PROTECT, verbose_name='Тип')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class receipt_has_product(models.Model):
    receipt_id = models.ForeignKey(receipt, on_delete=models.CASCADE, verbose_name='Заказ')
    product_id = models.ForeignKey(product, on_delete=models.PROTECT, verbose_name='Товар')
    price = models.DecimalField('Цена', max_digits=40, decimal_places=2,
                                validators=[MinValueValidator(Decimal('0.01'))])
    amount = models.PositiveIntegerField('Количество', validators=[MinValueValidator(Decimal('1'))])

    class Meta:
        unique_together = ('receipt_id', 'product_id')
        verbose_name = 'Заказ-продукт'
        verbose_name_plural = 'Заказы-продукты'

    # def __str__(self):
    #     return self.product_id
