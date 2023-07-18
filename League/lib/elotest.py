K=32
def actualScore(diff):
    # Calculates the score between 0 to 1 from the goal difference
    # diff: goal difference
    # return: score between 0 and 1
    return bool(diff>0)
    #return 1-1/(1+diff)

def combinedElo(eloA,eloB):
    # Calculates the combined elo of two players
    # eloA: elo of player A
    # eloB: elo of player B
    # return: combined elo
    return (eloA+eloB)/2
def expectedScore(eloA,eloB):
    # Calculates the expected score of player A
    # eloA: elo of player A
    # eloB: elo of player B
    # return: expected score between 0 and 1
    return 1/(1+10**((eloB-eloA)/400))

def eloChange(eloA,eloB,diff):
    # Calculates the change of elo
    # eloA: elo of player A
    # eloB: elo of player B
    # diff: goal difference
    # return: new elo
    return K*(actualScore(diff)-expectedScore(eloA,eloB))

def teamEloChange(eloA1,eloA2,eloB1,eloB2,diff):
    # Calculates the change of elo for the first player of the first team
    # eloA1: elo of player A1
    # eloA2: elo of player A2
    # eloB1: elo of player B1
    # eloB2: elo of player B2
    # diff: goal difference
    # return: new elo of player A1
    eloA=combinedElo(eloA1,eloA2)
    eloB=combinedElo(eloB1,eloB2)

    return eloChange(eloA,eloB,diff)*((eloA2 if diff>0 else eloA1)/eloA)

def teamEloChanges(elos,diff):
    # Calculates the change of elo for all players in a tuple
    # elos: tuple of elos of all players
    # diff: goal difference
    # return: new elos of all players
    output=(
        teamEloChange(elos[0],elos[1],elos[2],elos[3],diff),
        teamEloChange(elos[1],elos[0],elos[2],elos[3],diff),
        teamEloChange(elos[2],elos[3],elos[0],elos[1],-diff),
        teamEloChange(elos[3],elos[2],elos[0],elos[1],-diff)
    )
    return output
print(teamEloChanges((200,1000,600,600),1))