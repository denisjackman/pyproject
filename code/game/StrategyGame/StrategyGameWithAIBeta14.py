#!/usr/bin/python
# -*- coding: utf-8 -*-
''''
    This version is made for AI. Copyrighted: NickandNicksGaming LLC
    Date modified = 3/29/2013
    Version: Beta 1.4
'''

import sys
import os
import os.path
import pickle

OPTIONS = ["BUILD (B)", "RESEARCH (R)", "TRAIN (T)", "DEPLOY (D)", "END (E)", "QUIT (Q)"]

def Won(wonplayer, reason):
    '''
        won function
    '''
    print(f"{wonplayer.name} wins, {reason}")
    won = True
    return won

class Player():
    '''
        player object
    '''
    def __init__(self, name, color):
        self.name = name
        self.color = color

        self.Mill = {'price':10, 'num':0, 'desc':"Collects 5 FOOD every turn with bonus."}
        self.Quarry = {'price':15, 'num':0, 'desc':"Collects 5 GOLD every turn with bonus."}
        self.LumberYard = {'price':15, 'num':1, 'desc':"Collects 5 WOOD every turn with bonus."}
        self.factory = {'price':50, 'num':0, 'desc':"Collects 20 of EVERY resource each turn NO BONUS."}
        self.Wonder = {'price':1000, 'num':0, 'desc':"Wins you the game."}

        self.spy = {'price':15, 'num':0, 'desc':"Lets you see opponent's resources, buildings, and advances."}
        self.raider = {'price':25, 'num':0, 'desc':"Destroys one of the most common building in enemy's base"}
        self.thief = {'price':20, 'num':0, 'desc':"Steals 5 of an opponents resource of your choice"}

        #self.sharperaxes = {'price':2, 'level':1, 'desc':"}        Dictionaries for advances. to add. too lazy.

        self.gold = {'num': 5, 'desc':"Used to research new advances for faster resource collection."}
        self.wood = {'num': 5, 'desc':"Used to build buildings."}
        self.food = {'num': 5, 'desc':"Used to train units."}

        #self.rescources = {'GOLD':5, 'WOOD':10, 'FOOD':5}
        self.resources = {'GOLD':self.gold, 'WOOD':self.wood, 'FOOD':self.food}
        self.buildings = {'MILL':self.Mill, 'QUARRY':self.Quarry, 'LUMBER YARD':self.LumberYard, 'FACTORY':self.factory, 'WONDER':self.Wonder}
        self.advances = {'SHARPER AXES':1, 'CROP ROTATION':1, 'SHARPER PICKS':1}
        self.units = {'SPY': self.spy, 'RAIDER':self.raider, 'THIEF':self.thief}

    def whoami(self):
        '''
            print name
        '''
        return self.name

    def purse(self):
        '''
            print wealth
        '''
        return self.gold

class AI(Player):
    '''
        AI object
    '''

    def turn(self, next_player):
        '''
            Turn function
        '''
        self.resources["FOOD"]["num"]+=self.buildings["MILL"]["num"]*5*self.advances['CROP ROTATION']+(self.buildings["FACTORY"]["num"]*20)
        self.resources["WOOD"]["num"]+=self.buildings["LUMBER YARD"]["num"]*5*self.advances['SHARPER AXES']+(self.buildings["FACTORY"]["num"]*20)
        self.resources["GOLD"]["num"]+=self.buildings["QUARRY"]["num"]*5*self.advances['SHARPER PICKS']+(self.buildings["FACTORY"]["num"]*20)
        food_done = False
        while food_done is False:
            if self.resources["FOOD"]["num"] >= 25:
                self.units["RAIDER"]["num"]+=1
                self.resources["FOOD"]["num"]-=25

            while self.units["RAIDER"]["num"] > 0:

                list1 = []
                for i in next_player.buildings:
                    list1.append((next_player.buildings[i]["num"], i))

                destroyed = max(list1)
                if destroyed[0]>0:
                    next_player.buildings[destroyed[1]]["num"]-=1
                    print(f"Enemy {destroyed[1]} destroyed!")
                    self.units["RAIDER"]["num"]-=1
                else:
                    print("Nothing to destroy!")
                    break

            food_done = True
        wood_done = False

        while wood_done is False:
            if self.resources["WOOD"]["num"] >= 1000:
                self.buildings["WONDER"]["num"]+=1
                self.resources["WOOD"]["num"] -= 1000
                won = Won(self, "Alpha built a WONDER")
                break
            print("debug 001 : ", self.resources["WOOD"]["num"], self.resources["WOOD"])
            if self.resources["WOOD"]["num"] >= 15:
                if self.buildings["LUMBER YARD"]["num"] == self.buildings["QUARRY"]["num"]:
                    if self.buildings["MILL"]["num"] < self.buildings["LUMBER YARD"]["num"]:
                        self.buildings["MILL"]["num"]+=1
                        self.resources["WOOD"]["num"]-=10
                    else:
                        self.buildings["LUMBER YARD"]["num"]+=1

                else:
                    min_build = min(self.buildings["LUMBER YARD"], self.buildings["QUARRY"])
                    if self.buildings["MILL"]["num"] == min_build["num"]:
                        self.buildings["MILL"]["num"]+=1
                        self.resources["WOOD"]["num"]-=10
                    else:
                        min_build["num"]+=1
                        self.resources["WOOD"]["num"]-=15

            elif int(self.resources["WOOD"]["num"])<15 and self.resources["WOOD"]["num"]>=10:
            # elif self.resources["WOOD"]<15 and self.resources["WOOD"]>=10:
                min_build = min(self.buildings["LUMBER YARD"]["num"], self.buildings["QUARRY"]["num"], self.buildings["MILL"]["num"])
                if self.buildings["MILL"]["num"] == min_build:
                    self.buildings["MILL"]["num"]+=1
                    self.resources["WOOD"]["num"]-=10
                    wood_done =True
                else:
                    wood_done = True

            else:
                wood_done = True

            gold_done = False

            while gold_done is False:

                if self.advances["SHARPER AXES"]== self.advances["SHARPER PICKS"] == self.advances["CROP ROTATION"]:
                    if self.resources["GOLD"]["num"] >= (self.advances["SHARPER AXES"]*2)**2:
                        self.resources["GOLD"]["num"]-=(self.advances["SHARPER AXES"]*2)**2
                        self.advances["SHARPER AXES"]+=1

                    else:
                        gold_done = True

                elif self.advances["SHARPER PICKS"] == self.advances["CROP ROTATION"]:
                    if self.resources["GOLD"]["num"] >= (self.advances["CROP ROTATION"]*2)**2:
                        self.resources["GOLD"]["num"]-=(self.advances["CROP ROTATION"]*2)**2
                        self.advances["CROP ROTATION"]+=1

                    else:
                        gold_done = True

                else:
                    if self.resources["GOLD"]["num"] >= (self.advances["SHARPER PICKS"]*2)**2:
                        self.resources["GOLD"]["num"]-=(self.advances["SHARPER PICKS"]*2)**2
                        self.advances["SHARPER PICKS"]+=1

                    else:

                        gold_done = True

def start():
    '''
        start function
    '''
    gamestart = False
    while gamestart is False:
        start_option = input("New game (N) or load a game (L)?: ").upper()

        if start_option in ("NEW GAME", "N"):
            os.system('cls')
            # clears screen
            os.system('color c')
            # Light red

            player1 = Player(input("What is your name Player 1?: ").upper(), 'a')
            # Light green
            player2 = AI("Alpha", 0)

            first, second = player1, player2
            gameWon = False
            gamestart = True
            turn = 0

        elif start_option in ("LOAD", "L"):

            raw_filenames = os.listdir("y:/pyproject/resources/saves/")

            save_files = []
            for name in raw_filenames:

                if name.endswith('.pkl'):
                    save_files.append(os.path.join("y:/pyproject/resources/saves/", name))

            if len(save_files) <1:
                print("No save files!")

            else:
                os.system('cls')
                save_files.reverse()
                print("Save Games:\n")
                for name in save_files:
                    print(name[8:][:-4]+"\n")

                save_option = input("What game would you like to load? (or BACK (B)): ").upper()
                if save_option in ("B", "BACK"):
                    os.system('cls')
                else:
                    try:
                        with open('y:/pyproject/resources/saves/'+save_option+'.pkl', 'rb') as opened_file:
                            data = pickle.load(opened_file)

                        second, first, gameWon, turn = data
                        gamestart = True
                    except Exception:
                        os.system('cls')
                        print("Not a valid name\n")

        else:
            print("try again\n")

    while gameWon is False:
        # pylint: disable=unbalanced-tuple-unpacking
        first, second, gameWon, turn = play_turn(player1, player2, gameWon, turn)
        player2.turn(player1)

    input("Hit enter to close. ")


def play_turn(current_player, next_player, turnWon, turn1):  # pylint: disable=too-many-locals
    '''
        Function play_turn
    '''
    turn1 += 1
    os.system('cls')
    os.system(f'color {current_player.color}')

    input(current_player.name+", hit enter to start turn.")

    turn = 1

    if current_player.name[-1] == 'S': #Just some proper grammer
        print(f"\nIt is {current_player.name} Turn\n")
    else:
        print(f"\nIt is {current_player.name}'s Turn\n")

    print(f"FOOD from MILLs: {current_player.buildings['MILL']['num']*5*current_player.advances['CROP ROTATION']}")
    print(f"WOOD from LUMBER YARDs: {current_player.buildings['LUMBER YARD']['num']*5*current_player.advances['SHARPER AXES']}")
    print(f"GOLD from QUARRYs: {current_player.buildings['QUARRY']['num']*5*current_player.advances['SHARPER PICKS']}")

    if current_player.buildings["FACTORY"]["num"] >0:
        print("fWOOD, FOOD, and GOLD from FACTORIES: {current_player.buildings['FACTORY']['num']*20}")

    current_player.food["num"]+=current_player.buildings["MILL"]["num"]*5*current_player.advances['CROP ROTATION']+(current_player.buildings["FACTORY"]["num"]*20)
    current_player.wood["num"]+=current_player.buildings["LUMBER YARD"]["num"]*5*current_player.advances['SHARPER AXES']+(current_player.buildings["FACTORY"]["num"]*20)
    current_player.gold["num"]+=current_player.buildings["QUARRY"]["num"]*5*current_player.advances['SHARPER PICKS']+(current_player.buildings["FACTORY"]["num"]*20)

    research = False

    while turn and turnWon is False:  # pylint: disable=too-many-nested-blocks
        if current_player.buildings["WONDER"]["num"]>0:
            turnWon = True
        if turnWon is True:
            input(str(current_player.name)+" Won! ")
            return(0, 0, turnWon)
        print("\nBuildings:")

        for i in current_player.buildings.keys():
            # Lists the player's buildings
            print(f"{str(i)} - {current_player.buildings[i]['num']}")

        print("\nAdvances:")

        for i in current_player.advances:
            # Lists the player's units
            print(f"{str(i)} - {current_player.advances[i]}")

        print("\nResources:")

        for i in current_player.resources:
            print(F"{str(i)} - {current_player.resources[i]['num']}")

        print("\nUnits:")

        for i in current_player.units:
            print(f"{str(i)} - {current_player.units[i]['num']}")


        print("\nYour OPTIONS are:\n")
        # list OPTIONS for the players turn.
        for i in OPTIONS:
            if i == OPTIONS[-1]:
                print(f"and {i} .")
            else:
                print(f"{i},")

        print("\n")

        choice = input("What do you want to do?: ").upper()
        print("\n")

        if choice in ("BUILD", "B"):
            # Build buildings to help supply resources
            print(f"WOOD: {str(current_player.resources['WOOD']['num'])}\n")
            for keys in current_player.buildings.keys():
                print(f"{keys}----------------")
                print("Current number: "+str(current_player.buildings[keys]["num"]))
                print("WOOD required to build: "+str(current_player.buildings[keys]["price"]))
                print(current_player.buildings[keys]["desc"])
                print("\n")

            build_choice = input("What would you like to build?: ").upper()
            print("\n")

            if build_choice in current_player.buildings:
                if current_player.resources["WOOD"]["num"]>=current_player.buildings[build_choice]["price"]:
                    current_player.resources["WOOD"]["num"]-=current_player.buildings[build_choice]["price"]
                    current_player.buildings[build_choice]["num"]+=1
                    print("Current WOOD: "+str(current_player.resources["WOOD"]["num"]))
                    print("Current number of "+str(build_choice)+":", current_player.buildings[build_choice]["num"])
                else:
                    print("Not enough WOOD!")
            else:
                print("Please choose a valid option.")

            input("\nPress enter to continue ")

        elif choice in ("RESEARCH", "R"):
            # Research advanced ways to gather resources
            print("GOLD: "+str(current_player.resources["GOLD"]["num"])+"\n")
            if research is False:
                for keys in current_player.advances.keys():
                    print(keys+"----------------")
                    print("Current level: "+str(current_player.advances[keys]))
                    print("GOLD required to upgrade: "+str((current_player.advances[keys]*2)**2))
                    print("\n")

                research_choice = input("What would you like to upgrade?: ").upper()
                print("\n")
                if research_choice in current_player.advances:
                    if current_player.resources["GOLD"]["num"]>=(current_player.advances[research_choice]*2)**2:
                        current_player.resources["GOLD"]["num"]-=(current_player.advances[research_choice]*2)**2
                        current_player.advances[research_choice]+=1
                        print("Current GOLD: "+str(current_player.resources["GOLD"]["num"]))
                        print("Current",research_choice,"level:", current_player.advances[research_choice])
                        # research = True
                    else:
                        print("Not enough GOLD!")
                else:
                    print("Please choose a valid option.")
            elif research:
                print("You can only research one thing per turn!")

            input("\nPress enter to continue ")

        elif choice in ("TRAIN", "T"):
            print("FOOD: "+str(current_player.resources["FOOD"]["num"])+"\n")
            for keys in current_player.units.keys():
                print(keys+"----------------")
                print("FOOD required to use: "+str(current_player.units[keys]["price"]))
                print(current_player.units[keys]["desc"])
                print("\n")

            train_choice = input("What would you like to train?: ").upper()
            if train_choice in current_player.units:
                if current_player.resources["FOOD"]["num"]>=current_player.units[train_choice]["price"]:
                    current_player.resources["FOOD"]["num"]-=current_player.units[train_choice]["price"]
                    current_player.units[train_choice]["num"]+=1
                    print("Current FOOD: "+str(current_player.resources["FOOD"]["num"]))
                    print("Current "+train_choice+":",current_player.units[train_choice]["num"])
                else:
                    print("Not enough FOOD!")
            else:
                print("Please choose a valid option.")

            input("\nPress enter to continue ")

        elif choice in ("DEPLOY", "D"):
            for i in current_player.units:
                print(i, current_player.units[i]["num"])

            deploy_choice = input("What would you like to deploy?: ").upper()
            print("\n")

            if deploy_choice in current_player.units and current_player.units[deploy_choice]["num"]>0:
                if deploy_choice == "SPY":
                    print("*REPORT*\n*ENEMY HAS*\n")
                    for i in next_player.buildings:
                        print(i, next_player.buildings[i]["num"])
                    for i in next_player.resources:
                        print(i, next_player.resources[i]["num"])
                    for i in next_player.advances:
                        print(i, next_player.advances[i])
                    print("/n*END REPORT*")

                    current_player.units["SPY"]["num"]-=1

                elif deploy_choice == "RAIDER">0:
                    list1 = []
                    for i in next_player.buildings:
                        list1.append((next_player.buildings[i]["num"], i))

                    destroyed = max(list1)
                    if destroyed[0]>0:
                        next_player.buildings[destroyed[1]]["num"]-=1
                        print(f"Enemy {destroyed[1]} destroyed!")
                        current_player.units["RAIDER"]["num"]-=1
                    else:
                        print("Nothing to destroy!")

                elif deploy_choice == "THIEF">0:
                    available_resources = []
                    for i in next_player.resources:
                        if next_player.resources[i]["num"]>=5:
                            available_resources.append(i)

                    if len(available_resources)>0:
                        print("You could steal 5 of:")
                        for i in available_resources:
                            print(i)
                    else:
                        print("Nothing to steal!")

                    succeded = False
                    if len(available_resources)>0:
                        while succeded is False:
                            steal = input("What would you like to steal?: ").upper()
                            if steal in available_resources:

                                next_player.resources[steal]["num"]-=5
                                current_player.resources[steal]["num"]+=5
                                succeded = True

                            else:
                                print("Error")

                            if succeded is True:
                                current_player.units["THIEF"]["num"]-=1

            input("\nPress enter to continue ")

        elif choice in ("END", "E"):
            turn = False
            everything = [current_player, next_player, Won, turn]

            with open('y:/pyproject/resources/saves/'+current_player.name[:6]+next_player.name[:6]+str(turn1)+'.pkl', 'wb') as output:
                pickle.dump(everything, output, -1)

        elif choice in ("QUIT", "Q"):
            sys.exit("QUITTING")
        print("Not an option")

    if turn==0:
        input("\nHit enter to end your turn. ")
        return(next_player, current_player, Won, turn1)



if __name__ == '__main__':
    start()
