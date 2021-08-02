# Generated by Django 3.2 on 2021-05-31 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210531_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='delivery_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип доставки',
                'verbose_name_plural': 'Типы доставок',
            },
        ),
        migrations.CreateModel(
            name='receipt_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Статус заказа',
                'verbose_name_plural': 'Статусы заказов',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='role_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.role', verbose_name='Роль'),
        ),
    ]