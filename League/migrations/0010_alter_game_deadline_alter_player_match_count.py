# Generated by Django 4.2.3 on 2023-07-19 11:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('League', '0009_remove_player_preffered_position_player_match_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 2, 11, 40, 30, 422915, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='player',
            name='match_count',
            field=models.IntegerField(default=0),
        ),
    ]
