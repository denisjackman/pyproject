'''
    placeholder for equipment class
'''

class Equipment:
    '''
        equipment class
    '''
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost

    def __str__(self):
        '''
            return the item name
        '''
        return self.name

    def weigh(self):
        '''
            return the weight of the item in WU
        '''
        return self.weight

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
