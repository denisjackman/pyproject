'''
    test the dice
'''
import os
import sys
# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.DndProject.dnddice import dice

if __name__ == "__main__":
    print(f" Dice roll one six sided     : {str(dice())}")
    print(f" Dice roll one hundred sided : {str(dice(100))}")
    print(f" Dice roll five six sided    : {str(dice(rolls=5))}")
    print(f" Dice roll ten four sided    : {str(dice(4, 10))}")
