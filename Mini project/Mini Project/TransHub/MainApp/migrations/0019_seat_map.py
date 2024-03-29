# Generated by Django 4.2.7 on 2024-02-21 10:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0018_delete_seat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat_map',
            fields=[
                ('seat_number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('booked_seat', models.BooleanField(default=False)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.bus')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.schedule')),
            ],
        ),
    ]
