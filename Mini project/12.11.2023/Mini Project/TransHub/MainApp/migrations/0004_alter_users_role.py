# Generated by Django 4.2.5 on 2023-10-30 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_users_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(default='USER', max_length=15),
        ),
    ]
