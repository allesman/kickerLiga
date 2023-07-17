# Generated by Django 4.2.3 on 2023-07-17 14:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('preffered_position', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_diff', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('deadline', models.DurationField(default=datetime.date(2023, 7, 31))),
                ('player_1A', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_1A', to='League.player')),
                ('player_1B', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_1B', to='League.player')),
                ('player_2A', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_2A', to='League.player')),
                ('player_2B', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_2B', to='League.player')),
            ],
        ),
        migrations.CreateModel(
            name='Elo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('value', models.IntegerField(default=1000)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='League.player')),
            ],
        ),
    ]