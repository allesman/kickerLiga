from random import sample

from League.models import Player, Game
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
        # TODO: Preffered Position is not considered
        for i in range(0,len(shuffled),4):
            self.new_match(shuffled[i],shuffled[i+1],shuffled[i+2],shuffled[i+3])
            # note: this will fail if the number of players is not a multiple of 4
    def new_match(self,player_1A,player_1B,player_2A,player_2B):
        print(f"Created match with {player_1A.first_name}/{player_1B.first_name} vs {player_2A.first_name}/{player_2B.first_name}")
        # save match in db
        return Game.objects.create(player_1A=player_1A,player_1B=player_1B,player_2A=player_2A,player_2B=player_2B)

        
    def delete_unplayed():
        pass

    def create_example_players(self):
        self.delete_all()
        return Player.objects.bulk_create([
            Player(first_name="Merlin",last_name="Mustermann",email="",is_active=True,preffered_position=0),
            Player(first_name="Gandalf",last_name="Mustermann",email="",is_active=True,preffered_position=0),
            Player(first_name="Harry",last_name="Mustermann",email="",is_active=True,preffered_position=0),
            Player(first_name="Hermine",last_name="Mustermann",email="",is_active=True,preffered_position=0),
        ])
    
    def delete_all(self):
        Game.objects.all().delete()
        Player.objects.all().delete()