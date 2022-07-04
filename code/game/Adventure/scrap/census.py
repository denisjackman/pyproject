class Person:
    age = 15
    name = "Rolf"
    favorite_foods = ['beets','turnips','weisswurst']


    def birth_year(self):
        return 2015 - age

people = [Person(), Person(), Person() ]
sum = 0
for person in people:
    sum = sum + person.age
print "average age is : " + str(sum/len(people))