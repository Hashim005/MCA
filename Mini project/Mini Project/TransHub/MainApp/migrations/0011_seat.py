# Generated by Django 4.2.7 on 2023-12-02 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0010_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.IntegerField()),
                ('is_female_only', models.BooleanField(default=False)),
                ('is_booked', models.BooleanField(default=False)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.bus')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.schedule')),
            ],
        ),
    ]
