'''
    play python script
'''
# Global variables
GAMETITLE="TestGame001"
GAMEYEAR="2012"
GAMECOMPANY="MARSYS Games"

# Functions
def introScreen():
    '''
        intro screen
    '''
    print (GAMECOMPANY+' Presents '+str(GAMETITLE))
    print ('Copyright '+GAMECOMPANY+' '+str(GAMEYEAR))


def finishScreen():
    '''
        finish screen
    '''
    print (GAMECOMPANY+' thanks you for playing '+GAMETITLE )
    print ('Bye!')


#main program loop
introScreen()
finishScreen()
