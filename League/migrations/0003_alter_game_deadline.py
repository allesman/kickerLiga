# Generated by Django 4.2.3 on 2023-07-18 08:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('League', '0002_alter_game_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 1, 8, 12, 25, 99718)),
        ),
    ]
