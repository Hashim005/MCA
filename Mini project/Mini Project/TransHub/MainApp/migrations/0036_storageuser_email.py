# Generated by Django 4.2.7 on 2024-04-01 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0035_storageuser_storagemap'),
    ]

    operations = [
        migrations.AddField(
            model_name='storageuser',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
    ]
