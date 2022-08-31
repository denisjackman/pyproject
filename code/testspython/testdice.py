'''
    test the dice
'''
from djgamemodule import dice as rpg

if __name__ == "__main__":
    print(" Dice roll one six sided     : " + str(rpg.dice()))
    print(" Dice roll one hundred sided : " + str(rpg.dice(100)))
    print(" Dice roll five six sided    : " + str(rpg.dice(rolls=5)))
    print(" Dice roll ten four sided    : " + str(rpg.dice(4,10)))
