'''
    placeholder for equipment class
'''


class Equipment:
    '''
        equipment class
    '''
    def __init__(self):
        raise NotImplementedError("Do Not create raw Equipment objects")

    def __str__(self):
        '''
            return the item name
        '''
        return self.name

    def weighs(self):
        '''
            return the weight of the item in WU
        '''
        return self.weight

    def cost(self):
        '''
            return the cost of the item in GP
        '''
        return self.cost


class Clothes(Equipment):
    '''
        Clothes class
    '''
    def __init__(self):
        self.name = "Clothes"
        self.weight = 10
        self.cost = 5
        self.plural = "Clothes"
        self.number = 1


class Provision(Equipment):
    '''
        Provision class
    '''
    def __init__(self):
        self.name = "Provision"
        self.weight = 20
        self.cost = 10
        self.plural = "Provisions"
        self.number = 1


class DelversPackage(Equipment):
    ''' Delvers Package class '''
    def __init__(self):
        self.name = "Delver's Package"
        self.weight = 20
        self.cost = 20
        self.plural = "Delver's Packages"
        self.number = 1


class Torch(Equipment):
    ''' Torch class '''
    def __init__(self):
        self.name = "Torch"
        self.weight = 10
        self.cost = 0.1
        self.plural = "Torches"
        self.number = 1


class RopeSilk(Equipment):
    ''' Rope, Silk, 1ft class '''
    def __init__(self):
        self.name = "Rope, Silk"
        self.weight = 1
        self.cost = 1
        self.plural = "Rope, Silk"
        self.number = 1


class RopeHemp(Equipment):
    ''' Rope, Hemp, 1ft class '''
    def __init__(self):
        self.name = "Rope, Hemp"
        self.weight = 5
        self.cost = 0.1
        self.plural = "Rope, Hemp"
        self.number = 1


class LanternOil(Equipment):
    ''' Lantern and Oil class '''
    def __init__(self):
        self.name = "Oil Lantern"
        self.weight = 10
        self.cost = 0.1
        self.plural = "Oil Lanterns"
        self.number = 1


class OilFlask(Equipment):
    ''' Oil Flask class '''
    def __init__(self):
        self.name = "Oil Flask"
        self.weight = 15
        self.cost = 10
        self.plural = "Oil Flasks"
        self.number = 1


class MagneticCompass(Equipment):
    ''' Magnetic Compass class '''
    def __init__(self):
        self.name = "Magnetic Compass"
        self.weight = 1
        self.cost = 15
        self.plural = "Magnetic Compasses"
        self.number = 1


class BootsKneeHigh(Equipment):
    ''' Boots, knee high class '''
    def __init__(self):
        self.name = "Knee High Boots"
        self.weight = 40
        self.cost = 10
        self.plural = "Knee High Boots"
        self.number = 1


class BootsCalfHigh(Equipment):
    ''' Boots, calf high class '''
    def __init__(self):
        self.name = "Calf High Boots"
        self.weight = 20
        self.cost = 5
        self.plural = "Calf High Boots"
        self.number = 1


class Sandals(Equipment):
    ''' Sandals class '''
    def __init__(self):
        self.name = "Sandals"
        self.weight = 2
        self.cost = 2
        self.plural = "Sandals"
        self.number = 1


class Piton(Equipment):
    ''' Piton class '''
    def __init__(self):
        self.name = "Piton"
        self.weight = 25
        self.cost = 10
        self.plural = "Pitons"
        self.number = 10


class PitonHammer(Equipment):
    ''' Piton Hammer class '''
    def __init__(self):
        self.name = "Piton Hammer"
        self.weight = 25
        self.cost = 4
        self.plural = "Piton Hammers"
        self.number = 1


class OrdinaryMagicStaff(Equipment):
    ''' Ordinary Magic Staff class '''
    def __init__(self):
        self.name = "Ordinary Magic Staff"
        self.weight = 30
        self.cost = 100
        self.plural = "Ordinary Magic Staves"
        self.number = 1


class DeluxeMagicStaff(Equipment):
    ''' Deluxe Magic Staff class '''
    def __init__(self):
        self.name = "Deluxe Magic Staff"
        self.weight = 30
        self.cost = 5000
        self.plural = "Deluxe Magic Staves"
        self.number = 1


# equipment is listed as name, weight (in wu), cost (in gp)
# Name , Weight (in wu), Cost (in GP)
# "Warm dry clothing and Pack", 10, 5
# "Provisions", 20, 10
# "Delver's Package", 20, 20
# "Torch", 10, .1
# "Rope, Silk, 1ft", 1, 1
# "Rope, Hemp, 1ft", 5, .1
# "Lantern and Oil", .10, .1
# "Spare Skin of Oil", 15, 10
# "Magnetic compass", 1, 15
# "Boots, knee high", 40, 10
# "Boots, calf high", 20, 5
# "Sandals", 2, 2
# "Pitons (10)", 25, 10
# "Piton Hammer", 25, 4
# "Ordinary Magic Staff", 30, 100
# "Deluxe Magic Staff", 30, 5000
