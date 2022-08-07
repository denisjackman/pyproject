'''
    food generator
'''
import random
def dish():
    '''
        generate random food
    '''
    result = ''
    food=["onion","garlic","tomato","carrot","potatoe","mushroom","zucchinni","pumpkin","cabbage","bean","egg","corn","spinach","cucumber","broccoli","pork","trout","bacon","ham","meat","chicken","beef","mustard","noodle","sausage","fish"]
    food_adj=["delicious","spicy","warm","special","good","bad","tasty","cold","hot"]
    food_type=["souffle","casserole","puree","porridge","stew","soup"]
    result =f"{food_adj[random.randint(0, len(food_adj) - 1)]} {food[random.randint(0, len(food) - 1)]} {food_type[random.randint(0, len(food_type) - 1)]} "
    return result

def main():
    '''
        main function
    '''
    for _ in range(10):
        print(dish())

# Main loops
if __name__ == "__main__":
    main()
