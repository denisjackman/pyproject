'''
    this is the holder for a weapons class
'''
class Weapon:
    '''
        weapons class
    '''
    def __init__(self,
                 name,
                 dice,
                 adds,
                 wpnstr,
                 dex,
                 cost,
                 weight,
                 wpnrange = 0,
                 handed = False):
        self.name = name
        self.dice = dice
        self.adds = adds
        self.strength = wpnstr
        self.dexterity = dex
        self.cost = cost
        self.weight = weight
        self.range = wpnrange
        self.handed = handed

    def __str__(self):
        return self.name

    def double_handed(self):
        '''
            is the weapon two handed
        '''
        return self.handed

    def weighs(self):
        '''
            weight of weapon in WU
        '''
        return self.weight
# WEAPONS
# Name,Dice,Adds,Weapon Strength,Dexterity,Cost (in Gold), Weigth (in wu), Range (in yards),Doublehanded (Boolean - True or False)
# "Bludgeon",3,0,5,2,15,50
# "Broadsword",3,4,15,10,70,120
# "Common Spear",3,1,8,8,22,50,40
# "Crossbow",5,0,15,10,250,180,100,True
# "Dirk",2,1,1,4,18,16,10
# "Doublebitted Axe",6,3,21,10,140,220,0,True
# "Falchion",4,4,12,13,75,110
# "Great Sword",6,0,21,18,120,170,0,True
# "Heavy Mace",5,2,17,3,120,200,0,True
# "Medium Longbow",4,3,15,15,100,60,140,True
# "Quarterstaff",2,0,2,8,10,50,0,True
# "Sax (Dagger)",2,5,7,10,30,25
# "Scimitar",4,0,10,11,60,100
# "Short Sword",3,0,7,3,35,30
# "Trident",4,3,10,10,60,75,10
# "Very Light Bow",2,0,9,15,50,30,60,True
