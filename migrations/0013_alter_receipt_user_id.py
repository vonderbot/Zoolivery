# Generated by Django 3.2 on 2021-05-31 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210531_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='user_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.user', verbose_name='Пользователь'),
        ),
    ]
