# Generated by Django 5.1.4 on 2025-01-13 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('phone', 'Phone'), ('accessory', 'Accessory'), ('laptop', 'Laptop')], default='phone', max_length=50),
        ),
    ]