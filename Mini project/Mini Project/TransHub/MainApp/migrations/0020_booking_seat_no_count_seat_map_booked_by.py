# Generated by Django 4.2.7 on 2024-02-22 04:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0019_seat_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='seat_no_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='seat_map',
            name='booked_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
