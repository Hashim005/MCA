# Generated by Django 4.2.7 on 2024-02-16 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0015_booking_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='total_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
