# Generated by Django 4.2.3 on 2023-07-20 08:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('League', '0013_alter_game_deadline_alter_player_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 3, 8, 29, 0, 736530, tzinfo=datetime.timezone.utc)),
        ),
    ]
