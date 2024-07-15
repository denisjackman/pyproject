'''  this is a a game loop shell'''

# Imports

# Variables
GAMEMODETEST = True
GAMESTATE = "Init"
# the game has three states Init Main End
GAMERUN = True


def GameInit():
    ''' this is the function to initialize the game'''
    print("Game Init")


def GameMainLoop():
    ''' this is the function to run the game'''
    print("Game Main Loop")
    while GAMERUN:
        print("Main loop")


def GameTerminate():
    ''' this is the function to terminate the game'''
    print("Game Terminate")


def main():
    ''' this is the main function '''
    print("Main")
    GameInit()
    GameMainLoop()
    GameTerminate()


if __name__ == "__main__":
    main()
