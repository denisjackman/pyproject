'''
    elorating
'''
import math

def newRating(player_rating, opponent_rating, gametype):
    '''
        ELO rating system
    '''
    chance_of_winning = int((1/(1+(math.pow(10,((opponent_rating - player_rating)/400)) )))*100)
    chance_of_losing = 100 - chance_of_winning
    k_factor = 32
    win_points = int(round(k_factor * (chance_of_losing/100.0)))
    lose_points = int(round(k_factor * (chance_of_winning/100.0)))
    if gametype=="Win":
        result = player_rating + win_points
    else:
        result = player_rating - lose_points
    return result

PLAYERA = 1000
PLAYERB = 1000
print(f" A ({str(PLAYERA)}) vs B ({str(PLAYERB)})")
OPLAYERA = newRating(PLAYERA,PLAYERB,"Win")
OPLAYERB = newRating(PLAYERA,PLAYERB,"Lose")
PLAYERA=OPLAYERA
PLAYERB=OPLAYERB
print(f" A ({str(PLAYERA)}) vs B ({str(PLAYERB)})")
OPLAYERA = newRating(PLAYERA,PLAYERB,"Win")
OPLAYERB = newRating(PLAYERA,PLAYERB,"Lose")
PLAYERA=OPLAYERA
PLAYERB=OPLAYERB
print(f" A ({str(PLAYERA)}) vs B ({str(PLAYERB)})")
