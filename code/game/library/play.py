'''
    play python script
'''
# Global variables
GAMETITLE = "TestGame001"
GAMEYEAR = "2012"
GAMECOMPANY = "MARSYS Games"


def introScreen():
    '''
        intro screen
    '''
    print(f'{GAMECOMPANY} Presents {GAMETITLE}')
    print(f'Copyright {GAMECOMPANY} {GAMEYEAR}')


def finishScreen():
    '''
        finish screen
    '''
    print(f'{GAMECOMPANY} thanks you for playing {GAMETITLE}')
    print('Bye!')


def main():
    '''
        main function
    '''
    introScreen()
    finishScreen()


if __name__ == '__main__':
    main()
