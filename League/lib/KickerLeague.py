from random import sample
from django.utils import timezone
from django.db import models
from League.models import Player, Game, Elo
# class KickerLeague:
    # example = []
    # def __init__(self):
    #     self.create_example_players()
    #     self.new_match_day()

def new_match_day():
    # get active players in random order
    players=Player.objects.filter(is_active=True)
    # update match count
    for player in players:
            player.match_count=Game.objects.filter(models.Q(player_1A=player) | models.Q(player_1B=player) | models.Q(player_2A=player) | models.Q(player_2B=player)).count()
            player.save()
    # sort players by match count
    players = sorted(players,key=lambda player: player.match_count, reverse=True)
    # cut off unpaired players
    unpairedCount=len(players)%4
    unpaired = players[:unpairedCount]
    players = players[unpairedCount:]
    if unpairedCount>0:
        print("The following "+str(unpairedCount)+" players are unpaired:"+str(unpaired))
    # shuffle players
    players = sample(players,len(players))
    # get number of matchday, if there are no valid matches yet, start with 1
    lastmatch = Game.objects.all().order_by("-matchday").first()
    if lastmatch is None or lastmatch.matchday is None:
        matchday = 1
    else:
        matchday = lastmatch.matchday+1
    print("Creating match day "+str(matchday))
    # create matches
    for i in range(0,len(players),4):
        new_match(players[i],players[i+1],players[i+2],players[i+3],matchday=matchday)
def new_match(player_1A,player_1B,player_2A,player_2B,matchday=None):
    print(f"Created match with {player_1A.first_name}/{player_1B.first_name} vs {player_2A.first_name}/{player_2B.first_name}")
    # save match in db
    return Game.objects.create(player_1A=player_1A,player_1B=player_1B,player_2A=player_2A,player_2B=player_2B,matchday=matchday)

    # def get_scoreboard(self):
    #     # get latest elo for each player, together with player name
    #     # not necessary, because scoreboard is already implemented in the frontend
    #     elos = [Elo.objects.filter(player=player).order_by('-timestamp').first() for player in Player.objects.all()]
    #     elos = {k:v for k,v in zip([elo.player.first_name for elo in elos], [elo.value for elo in elos])}
    #     elos = {k:v for k, v in sorted(elos.items(), key=lambda item: item[1],reverse=True)}
    #     print(elos)
    #     return elos

def delete_unplayed():
    Game.objects.filter(goal_diff__isnull=True,deadline__lt=timezone.now()).delete()

def create_example_players(self):
    self.delete_all()
    for i in range(4):
        Player.objects.create(first_name="Merlin"+str(i+1),last_name="Mustermann",email="",is_active=True,preffered_position=0),

def delete_all(self):
    Game.objects.all().delete()
    Player.objects.all().delete()
    Elo.objects.all().delete()
