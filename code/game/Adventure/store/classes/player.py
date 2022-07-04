class Player:
    def __init__(self):
        raise NotImplementedError("Do not create raw Player Objects")

    def __str__(self):
        return self.name
    name = ""
    type = ""  # this will be the professions (Warrior, wizard, rogue etc)
    race = ""  # Kin: Race: This will one of the racial types as outlines in the race list
    level = 1  # level always starts at 1
    strength = 0
    intelligence = 0
    luck = 0
    constitution = 0
    dexterity = 0
    charisma = 0
    additional = 0
    height = 0
    weight = 0
    weight_possible = 0
    weight_carried = 0
    gold = 0
    experience = 0
    weapons = []
    armour = []
    languages = []
    magic = ""
    other = []
