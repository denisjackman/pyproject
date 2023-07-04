#!/usr/bin/python 
'''
Imports
'''
import os 
import datetime 

'''
Variables 
'''
GameModeTest=True
GameState="Init" # the game has three states Init Main End 
GameRun=True

'''
Functions 
'''
def GameInit():
    print"GameInit"
    return
def GameMainLoop():
    print "GameMainLoop"
    while GameRun:
        print "Main loop"    
    return
def GameTerminate():
    print "GameTerminate"
    return

'''
Main Loop 
'''
GameInit
GameMainLoop
GameTerminate
