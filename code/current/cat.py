'''
    cat class
'''


class Cat():
    '''
        cat class
    '''
    def __init__(self, new_name):
        '''
            init
        '''
        self.name = new_name
        self.color = ""
        self.weight = 0
        print("A kitten Lives!")

    def meow(self):
        '''
            meow
        '''
        print(self.name, "says Meow")

    def purr(self):
        '''
            purr
        '''
        print(self.name, "purrs ")


class Monster():
    '''
        monster class
    '''
    def __init__(self, new_name):
        self.name = new_name
        self.health = 0
        print("What have you done ?")

    def decrease_health(self, amount):
        '''
            decrease health
        '''
        self.health = self.health - amount
        if self.health < 0:
            print(self.name, "is dead!")

    def cast_magic(self):
        '''
            casts magic
        '''
        print(self.name, "casts a spell")


class BigCat(Cat):
    '''
        big cat inherits little cat
    '''
    def growl(self):
        '''
            growl function
        '''
        print(self.name, "Roars")


def main():
    '''
        main function
    '''
    my_cat = BigCat("Frankie")
    my_cat.color = "Tabby"
    my_cat.weight = 1.17
    my_cat.meow()
    my_cat.purr()
    my_cat.growl()

    my_monster = Monster("Frankie-stein")
    my_monster.health = 100
    my_monster.cast_magic()
    my_monster.decrease_health(110)


if __name__ == '__main__':
    main()
