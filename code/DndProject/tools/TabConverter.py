'''
    this converts a tab file into a json file
'''
import json
    # generate the random numbers based on the len of the lists
    # build the results

def main():
    '''
        main function
    '''
    names = ["hawk","fair","spear","eagle","sea","dreamer","black","stone","singer","dark","fox","bow",
             "blade","death","high","grey","changer","strong","wood","white","bear","star","sly","claw",
             "sure","slayer","helm","staff","gold","wave","shadow","tiger","shield","brother","cleaver",
             "sky","dancer","flame","bone","moon","lion","foam","red","horn","soul","silver","fang","fist",
             "wolf","blood","bane","free","rune","wise","hammer","storm","piper","weaver","heart","wind"]
    prefix = ["bird","crystal","dove","earth","fast","flame","glitter","gold","golden","hawk","honor","ice",
              "iron","lightning","maple","moon","oak","raven","river","shadow","silver","sly","small","snow",
              "star","steel","stone","sun","swift","wild","willow","wind","winter"]
    suffix = ["bird","bones","caller","child","cloak","dancer","dove","eye","flower","fox","gold","hand","hawk",
              "heart","lady","leaf","light","lover","raven","shadow","singer","song","foot","man","skin",
              "strider","wanderer","whisper","will","wind"]

    with open("Y:/Resources/dnd/BarbarianNames.json", "w", encoding='utf8') as file:
        json.dump({"barbarian_names": names, "barbarian_prefix": prefix, "barbarian_suffix": suffix}, file)
    print(f"names: {len(names)} prefix: {len(prefix)} suffix: {len(suffix)}")

if __name__ == "__main__":
    main()
