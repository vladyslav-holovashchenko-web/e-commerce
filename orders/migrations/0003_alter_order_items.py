# Generated by Django 5.1.4 on 2024-12-17 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_initial'),
        ('orders', '0002_alter_order_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='cart.cartitem'),
        ),
    ]
