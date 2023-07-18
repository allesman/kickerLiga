import datetime
from typing import Iterable, Optional
from django.db import models
from django.utils import timezone



class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    preffered_position = models.IntegerField(default=0)

    def save(self,*args,**kwargs):
        # create elo entry if not exists
        if not Elo.objects.filter(player=self).exists():
            Elo.objects.create(player=self)
        super(Player,self).save(*args,**kwargs)

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
    deadline = models.DateTimeField(default=timezone.now()+timezone.timedelta(days=14))

    def save(self,*args,**kwargs):
        print("saving game")
        # set new timestamp
        self.timestamp = timezone.now()
        # check if game is played (goal_diff is not null)
        if self.goal_diff is not None:
            # calculate new elo
            # get old elo
            elo_1A = Elo.objects.filter(player=self.player_1A).order_by('-timestamp').first()
        super(Game,self).save(*args,**kwargs)