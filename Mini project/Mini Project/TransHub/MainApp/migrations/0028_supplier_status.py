# Generated by Django 4.2.7 on 2024-03-14 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0027_stock_supplier_delete_product_stock_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]
