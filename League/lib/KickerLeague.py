from random import sample

from League.models import Player, Game
class KickerLeague:
    # example = []
    def __init__(self):
        pass

    def new_match_day(self):
        # get active players
        players=Player.objects.filter(is_active=True)
        print(players)
        # shuffle players
        shuffled=sample(players,4)
        # create matches
        for i in range(0,len(players),4):
            self.new_match(players[i],players[i+1],players[i+2],players[i+3])
            # note: this will fail if the number of players is not a multiple of 4
        pass
    def new_match(self,player_1A,player_1B,player_2A,player_2B):
        print(f"Created match between {player_1A} / {player_1B} and {player_2A} / {player_2B}")
        # save match in db
        return Game.objects.create(player_1A=player_1A,player_1B=player_1B,player_2A=player_2A,player_2B=player_2B)

        
    def delete_unplayed():
        pass

    def create_example_players(self):
        return Player.objects.bulk_create([
            Player(first_name="Peter",last_name="Mustermann",email="",is_active=True,preffered_position=0),
            Player(first_name="Erika",last_name="Mustermann",email="",is_active=True,preffered_position=0),
            Player(first_name="Hans",last_name="Mustermann",email="",is_active=True,preffered_position=0),
            Player(first_name="Gretel",last_name="Mustermann",email="",is_active=True,preffered_position=0),
        ])
    
    def delete_all_players(self):
        return Player.objects.all().delete()