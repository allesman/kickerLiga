# Generated by Django 4.2.3 on 2023-07-18 08:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('League', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='deadline',
            field=models.DateTimeField(default=datetime.date(2023, 8, 1)),
        ),
    ]
