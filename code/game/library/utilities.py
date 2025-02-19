'''
    Utilities
'''

GAMEMODETEST = True
GAMESTATE = "Init"
# the game has three states Init Main End
GAMERUN = True


def GameInit():
    '''
        games initialise
    '''
    print("GameInit")


def GameMainLoop():
    '''
        game main loop
    '''
    print("GameMainLoop")
    while GAMERUN:
        print("Main loop")


def GameTerminate():
    '''
        game terminate
    '''
    print("GameTerminate")


def main():
    '''
        main routine
    '''
    GameInit()
    GameMainLoop()
    GameTerminate()


if __name__ == '__main__':
    main()
