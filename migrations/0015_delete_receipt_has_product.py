# Generated by Django 3.2 on 2021-05-31 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_receipt_user_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='receipt_has_product',
        ),
    ]