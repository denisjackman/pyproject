'''
    person class
'''


class Person:
    '''
        person class
    '''
    age = 15
    name = "Rolf"
    favorite_foods = ['beets', 'turnips', 'weisswurst']

    def __str__(self):
        return self.name

    def birth_year(self):
        '''
            birth year
        '''
        return 2022 - self.age


people = [Person(), Person(), Person()]
TOTAL_SUM = 0
for person in people:
    TOTAL_SUM += person.age
print("average age is : " + str(TOTAL_SUM/len(people)))
