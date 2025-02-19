'''
    Magic Spells class

    based on Chapter 3 of Fantasy Wargaming by Martin Hackett

'''


class MagicSpell:
    ''' generic spell class '''
    def __init__(self):
        raise NotImplementedError("Do not create raw MagicSpell Objects")

    def __str__(self):
        return self.name

    def spell_type(self):
        '''
            type of spell
        '''
        return self.spelltype

    def get_cost(self):
        '''
            cost of spell
        '''
        return self.cost


class Bubble(MagicSpell):
    ''' Bubble class '''
    def __init__(self):
        self.name = "Bubble"
        self.spelltype = "Normal"
        self.cost = 1
        self.cast_time = 1
        self.duration = 3
        self.range = 0
        self.area = 0
        self.number_effected = 1
        self.effect = "Adds 5 to the target's defence factor"
        self.castscore = 95  # 95 or less to cast


class Hail(MagicSpell):
    ''' Hail class '''
    def __init__(self):
        self.name = "Hail"
        self.spelltype = "Storm"
        self.cost = 12
        self.cast_time = 4
        self.duration = 10
        self.range = 0
        self.area = 60
        self.number_effected = 20
        self.effect = "Unit moves at half speed and cannot fire missiles"
        self.castscore = 84
