from random import sample

from League.models import Player, Game, Elo
class KickerLeague:
    # example = []
    def __init__(self):
        pass

    def new_match_day(self):
        # get active players
        players=Player.objects.filter(is_active=True)
        #print(players)
        # shuffle players
        shuffled = players
        # sample(players,4)
        unpairedCount=len(shuffled)%4
        unpaired = shuffled[:unpairedCount]
        shuffled = shuffled[unpairedCount:]
        print("The following "+str(unpairedCount)+" players are unpaired:"+str(unpaired))
        # create matches
        # TODO: Prefered Position is not considered
        for i in range(0,len(shuffled),4):
            self.new_match(shuffled[i],shuffled[i+1],shuffled[i+2],shuffled[i+3])
            # note: this will fail if the number of players is not a multiple of 4
    def new_match(self,player_1A,player_1B,player_2A,player_2B,diff=None):
        print(f"Created match with {player_1A.first_name}/{player_1B.first_name} vs {player_2A.first_name}/{player_2B.first_name}")
        # save match in db
        return Game.objects.create(player_1A=player_1A,player_1B=player_1B,player_2A=player_2A,player_2B=player_2B,goal_diff=1)

    def get_scoreboard(self):
        # get latest elo for each player, together with player name
        elos = [Elo.objects.filter(player=player).order_by('-timestamp').first() for player in Player.objects.all()]
        elos = {k:v for k,v in zip([elo.player.first_name for elo in elos], [elo.value for elo in elos])}
        elos = {k:v for k, v in sorted(elos.items(), key=lambda item: item[1],reverse=True)}
        print(elos)
        return elos

    def delete_unplayed():
        pass

    def create_example_players(self):
        self.delete_all()
        for i in range(4):
            Player.objects.create(first_name="Merlin"+str(i+1),last_name="Mustermann",email="",is_active=True,preffered_position=0),
    
    def delete_all(self):
        Game.objects.all().delete()
        Player.objects.all().delete()
        Elo.objects.all().delete()
