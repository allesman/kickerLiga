import datetime
from typing import Iterable, Optional
from django.db import models
from django.utils import timezone

from League.lib import EloTools



class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    match_count = models.IntegerField(default=0)

    def save(self,*args,**kwargs):
        print("saving player")
        # create elo entry if none exists
        super(Player,self).save(*args,**kwargs)
        if not Elo.objects.filter(player=self).exists():
            Elo.objects.create(player=self)
            print("created elo entry")
        else:
            print("elo entry already exists")
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

class Elo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    value = models.IntegerField(default=1000) 
    # def __str__(self):
    #     return self.player.first_name + " " + self.player.last_name + ": " + str(self.value)
    class Meta:
        verbose_name = 'Elo'
        verbose_name_plural = 'Scoreboard'
    

class Game(models.Model):
    player_1A = models.ForeignKey(Player, on_delete=models.CASCADE,related_name='player_1A')
    player_1B = models.ForeignKey(Player, on_delete=models.CASCADE,related_name='player_1B')
    player_2A = models.ForeignKey(Player, on_delete=models.CASCADE,related_name='player_2A')
    player_2B = models.ForeignKey(Player, on_delete=models.CASCADE,related_name='player_2B')
    goal_diff = models.IntegerField(null=True,blank=True) # Difference of goals between team 1 and team 2, if null, game is not played yet
    timestamp = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(default=timezone.now()+timezone.timedelta(days=14))
    matchday = models.IntegerField(null=True,blank=True)
    def save(self,*args,**kwargs):
        # print("saving game")
        # set new timestamp
        # self.timestamp = timezone.now()
        # check if game is played (goal_diff is not null)
        if self.goal_diff is not None:
            # calculate new elo
            # get old elos
            elos = [Elo.objects.filter(player=player).order_by('-timestamp').first() for player in [self.player_1A,self.player_1B,self.player_2A,self.player_2B]]
            # print(elos)
            # get int values
            elos = [elo.value for elo in elos]
            # calculate new elos
            new_elos = EloTools.calculate_elos(elos,self.goal_diff)
            # print(new_elos)
            # save new elos
            for i,player in enumerate([self.player_1A,self.player_1B,self.player_2A,self.player_2B]):
                Elo.objects.create(player=player,value=new_elos[i])
            # if this is not a manually created game
            if self.matchday is not None: 
                # check if all games of matchday are played
                unplayed=Game.objects.filter(matchday=self.matchday,goal_diff__isnull=True)
                print(f"unplayed games: {unplayed}")
        elif self.matchday is not None:
            # increase match_count of players
            for player in [self.player_1A,self.player_1B,self.player_2A,self.player_2B]:
                player.match_count = player.match_count + 1
                player.save()


        super(Game,self).save(*args,**kwargs)