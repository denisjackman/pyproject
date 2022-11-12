'''
    Name : TabConverter.py

    Function :
    This is a converter for the Data items from TAB files to JSON files
    The TAB files are from the DnD 5e SRD
'''
__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.00 $"
__date__ = "$Date: 2022/11/01 00:00:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

from pathlib import Path
import json

FILEPATH = Path(__file__).parent

def main():
    '''
        main function
    '''
    action = ["attack","fury","revenge","vengeance"]
    adjective = ["color","dark","elemental","forbidden","forgotten","ghost","hidden","lost","nightmare","sinister","unknown","sunless"]
    building = ["abbey","citadel","forge","hall","keep","manor","maze","palace","shrine","steading","stockade","temple","tomb","tower","vault"]
    color = ["black","blue","gold","green","red","silver","white"]
    creature  = ["ass","bear","beast","boar","bull","cat","chicken","chimera","cock","cow","crab","demon","devil","dog","dragon","drake","duck","eagle","falcon","fox","frog","gargoyle","goat","griffon","hare","hawk","hog","horse","hound","lamb","lion","lizard","mare","monster","owl","ox","phoenix","pig","pony","rat","raven","rooster","serpent","shadow","shark","sheep","siren","snake","stag","stallion","swine","unicorn","vulture","wolf","wyrm","wyvern"]
    deity = ["Demogorgon","Freya","Odin","Orcus","Tharizdun"]
    element = ["air","blood","chaos","darkness","death","desolation","doom","earth","evil","fire","fury","good","horrors","light","madness","order","power","water"]
    escape = ["escape","flight"]
    geography = ["canyon","desert","forest","glacial rift","hill","lake","mountain","river","sea"]
    item = ["bones","crucible","gold","grimoire","helm","palm","pearl","plume","scepter","spear","sword","tome"]
    journey = ["descent into","expedition to","journey into","voyage to"]
    monster = ["creature","demon","drow","Fire Giant","Frost Giant","Hill Giant","kuo-toa","vampire"]
    name = ["Inverness","Saltmarsh","Tamoachan","Tegel","Tsojcanth","Amanhir","Anargon","Anargon","Bergoth","Bergoth","Cardandir","Cardandir","Earaldir","Earaldir","Eogard","Eogard","Estarion","Estarion","Haldor","Haldor","Hathhelm","Hathhelm","Heruos","Heruos","Lorlost","Lorlost","Lorwise","Lorwise","Marast","Marast","Morgil","Morgil","Morwyn","Morwyn","Pelgorn","Pelgorn","Saeron","Saeron","Sarathar","Sarathar","Sereden","Sereden","Tirith"]
    people = ["cultists","druids","dwellers","followers","masters","slavers","warriors","wizards"]
    person = ["necromancer","slave","sorcerer","thrall","warlock","witch"]
    place = ["caverns","caves","city","lair","mazes","mines","oasis","pits","undercity","wastes"]
    quest = ["In Search of the","Quest for the","Search for the"]
    region = ["Barrier Peaks","Borderlands","Depths of the Earth"]
    ruler = ["god","jarl","king","lord","master","queen"]
    secret = ["mystery","riddle","secret"]

    with open(f"{FILEPATH}/../referencedata/AdventureNames.json", "w", encoding='utf8') as file:
        json.dump({"adventure_action": action,
                   "adventure_adjective": adjective,
                   "adventure_building": building,
                   "adventure_color": color,
                   "adventure_creature": creature,
                   "adventure_deity": deity,
                   "adventure_element": element,
                   "adventure_escape": escape,
                   "adventure_geography": geography,
                   "adventure_item": item,
                   "adventure_journey": journey,
                   "adventure_monster": monster,
                   "adventure_name": name,
                   "adventure_people": people,
                   "adventure_person": person,
                   "adventure_place": place,
                   "adventure_quest": quest,
                   "adventure_region": region,
                   "adventure_ruler": ruler,
                   "adventure_secret": secret},
                  file,
                  indent=4,
                  ensure_ascii=False)

if __name__ == "__main__":
    main()
