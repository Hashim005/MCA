# Generated by Django 4.2.7 on 2024-02-16 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0016_alter_booking_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='total_price',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]