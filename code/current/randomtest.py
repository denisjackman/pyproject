'''
    randomtest.py
'''
import random
print(random.randint(0, 5))
print(random.random() * 100)
print(random.choice(["conan", "valeria", "belit"]))
lst = ["david", 44, "bdm publications", 3245, "pi", True, 3.14, "Python"]
rnd = random.choice(lst)
print(rnd)
random.shuffle(lst)
print(lst)
for i in range(20):
    print(random.randrange(0, 200, 7))
output = {"Heads": 0, "Tails": 0}
coins = list(output.keys())
for i in range(10000):
    output[random.choice(coins)] += 1
print("Heads : ", output["Heads"])
print("Tails : ", output["Tails"])
