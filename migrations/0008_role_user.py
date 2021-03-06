# Generated by Django 3.2 on 2021-05-30 11:32

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210530_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('description', models.CharField(max_length=500, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Роль',
                'verbose_name_plural': 'Роли',
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20, verbose_name='Логин')),
                ('password', models.CharField(max_length=20, verbose_name='Пароль')),
                ('name', models.PositiveIntegerField(verbose_name='Имя')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Телефон')),
                ('address', models.CharField(max_length=50, verbose_name='Адрес')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.role', verbose_name='Роль')),
            ],
            options={
                'verbose_name': 'Пользоваатель',
                'verbose_name_plural': 'Пользоваатели',
            },
        ),
    ]
