''' This file contains the connection string to the MongoDB Atlas cluster. '''
import os
import sys

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.dbfunctions.mongofunctions import open_mongo
from jackmanimation.dbfunctions.mongofunctions import insertData
from jackmanimation.dbfunctions.mongofunctions import getData
from jackmanimation.dbfunctions.mongofunctions import updateData
from jackmanimation.dbfunctions.mongofunctions import deleteData


def main():
    ''' main function '''
    print("[-] MongoDB Test Main start")
    client = open_mongo()
    datainsert = True
    datadelete = True
    datalist = []
    datalist.append({"_id": "U1IT00012",
                     "item_name": "even more new Stuff",
                     "category": "stuff",
                     "quantity": 12,
                     "price": 40,
                     "item_description": "a bunch of stuff"})
    if datainsert:
        insertData(client,
                   'user_shopping_list',
                   'user_1_items',
                   datalist)

    for item in getData(client,
                        'user_shopping_list',
                        'user_1_items'):
        if item['_id'] in ('U1IT00012',
                           'U1IT00011'):
            print(item)

    info = updateData(client,
                      'user_shopping_list',
                      'user_1_items',
                      'U1IT00011',
                      'item_name',
                      'Updated stuff')
    print(f"[-] Update Result is {info.modified_count}")
    if datadelete:
        info = deleteData(client,
                          'user_shopping_list',
                          'user_1_items',
                          'U1IT00012')
        print(f"[-] Delete Result is {info.deleted_count}")
    for item in getData(client,
                        'user_shopping_list',
                        'user_1_items'):
        if item['_id'] in ('U1IT00012',
                           'U1IT00011'):
            print(item)
    print("[-] MongoDB Test Main end")


if __name__ == '__main__':
    print("[+] Starting MongoDB Test")
    main()
    print("[+] MongoDB Test Complete")
