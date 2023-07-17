import datetime
from django.db import models


class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    preffered_position = models.IntegerField(default=0)

class Elo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    value = models.IntegerField(default=1000)

class Game(models.Model):
    player_1A = models.ForeignKey(Player, on_delete=models.CASCADE,related_name='player_1A')
    player_1B = models.ForeignKey(Player, on_delete=models.CASCADE,related_name='player_1B')
    player_2A = models.ForeignKey(Player, on_delete=models.CASCADE,related_name='player_2A')
    player_2B = models.ForeignKey(Player, on_delete=models.CASCADE,related_name='player_2B')
    goal_diff = models.IntegerField(null=True,blank=True) # Difference of goals between team 1 and team 2, if null, game is not played yet
    timestamp = models.DateTimeField(auto_now=True)
    deadline = models.DurationField(default=datetime.date.today()+datetime.timedelta(days=14))