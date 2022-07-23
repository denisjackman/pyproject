# Global variables
GameTitle="TestGame001"
GameYear="2012"
GameCompany="MARSYS Games"

# Functions 
def introScreen() :
    print (GameCompany+' Presents '+str(GameTitle))
    print ('Copyright '+GameCompany+' '+str(GameYear))
           
def finishScreen() :
    print (GameCompany+' thanks you for playing '+GameTitle )
    print ('Bye!')






#main program loop 
introScreen()
finishScreen()