# Generated by Django 5.1.4 on 2025-01-20 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.JSONField(default=list),
        ),
    ]
