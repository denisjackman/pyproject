''' utensils '''
import random
import json


def print_results(data):
    '''
        print the results function
    '''
    the_json = json.loads(data)
    if "title" in the_json["metadata"]:
        print(the_json["metadata"]["title"])
    count = the_json["metadata"]["count"]
    print(str(count) + " events recorded ")


def dish():
    '''
        generate random food
    '''
    result = ''
    food = ["onion",
            "garlic",
            "tomato",
            "carrot",
            "potatoe",
            "mushroom",
            "zucchinni",
            "pumpkin",
            "cabbage",
            "bean",
            "egg",
            "corn",
            "spinach",
            "cucumber",
            "broccoli",
            "pork",
            "trout",
            "bacon",
            "ham",
            "meat",
            "chicken",
            "beef",
            "mustard",
            "noodle",
            "sausage",
            "fish"]
    food_adj = ["delicious",
                "spicy",
                "warm",
                "special",
                "good",
                "bad",
                "tasty",
                "cold",
                "hot"]
    food_type = ["souffle",
                 "casserole",
                 "puree",
                 "porridge",
                 "stew",
                 "soup"]
    result = f"{food_adj[random.randint(0, len(food_adj) - 1)]} "\
             f"{food[random.randint(0, len(food) - 1)]} "\
             f"{food_type[random.randint(0, len(food_type) - 1)]} "
    return result


def right_justify(item):
    '''
    return a string that is right justified so the last
    character of item is in column 70
    '''
    result = ""
    result = f'{item:>70}'
    return result
