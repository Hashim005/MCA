# Generated by Django 4.2.7 on 2024-02-23 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0021_alter_seat_map_booked_by'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
