# the K factor is the maximum change of elo per game, as in the original elo system
K=32
# bonus elo for winning/losing
bonus=5
def actual_score(diff):
    # Calculates the score between 0 to 1 from the goal difference
    # diff: goal difference
    # return: score between 0 and 1
    # return bool(diff>0)
    return (diff+10)/20

def combined_elo(eloA,eloB):
    # Calculates the combined elo of two players
    # eloA: elo of player A
    # eloB: elo of player B
    # return: combined elo
    return (eloA+eloB)/2
def expected_score(eloA,eloB):
    # Calculates the expected score of player A
    # eloA: elo of player A
    # eloB: elo of player B
    # return: expected score between 0 and 1
    return 1/(1+10**((eloB-eloA)/400))

def elo_change(eloA,eloB,diff):
    # Calculates the change of elo
    # eloA: elo of player A
    # eloB: elo of player B
    # diff: goal difference
    # return: new elo
    return K*(actual_score(diff)-expected_score(eloA,eloB)) + (bonus if diff>0 else -bonus)

def team_elo_change(eloA1,eloA2,eloB1,eloB2,diff):
    # Calculates the change of elo for the player A1
    # eloA1: elo of player A1
    # eloA2: elo of player A2
    # eloB1: elo of player B1
    # eloB2: elo of player B2
    # diff: goal difference
    # return: change of elo for player A1
    eloA=combined_elo(eloA1,eloA2)
    eloB=combined_elo(eloB1,eloB2)

    return elo_change(eloA,eloB,diff)*((eloA2 if diff>0 else eloA1)/eloA)

def calculate_elos(elos,diff):
    # Calculates new elos for all players in a tuple
    # elos: tuple of elos of all players
    # diff: goal difference
    # return: new elos of all players

    # calling the team_elo_change function four times for each player
    # the order of the players is essential, since the first player
    # is the one whose elo is returned, the second player their teammate
    # and the third and fourth player their opponents
    output=(
        elos[0] + team_elo_change(elos[0],elos[1],elos[2],elos[3],diff),
        elos[1] + team_elo_change(elos[1],elos[0],elos[2],elos[3],diff),
        elos[2] + team_elo_change(elos[2],elos[3],elos[0],elos[1],-diff),
        elos[3] + team_elo_change(elos[3],elos[2],elos[0],elos[1],-diff)
    )
    return output