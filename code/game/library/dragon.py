'''
    dragon game
'''
import random
import time


def displayIntro():
    '''
        introduction function
    '''
    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()


def chooseCave():
    '''
        choose the cave
    '''
    cave = ''
    while cave not in ('1', '2'):
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave


def checkCave(chosenCave):
    '''
        check the cave
    '''
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')


def main():
    ''' main function '''
    PLAYAGAIN = 'yes'
    while PLAYAGAIN in ('yes', 'y'):

        displayIntro()

        caveNumber = chooseCave()

        checkCave(caveNumber)

        print('Do you want to play again? (yes or no)')
        PLAYAGAIN = input()


if __name__ == '__main__':
    main()
