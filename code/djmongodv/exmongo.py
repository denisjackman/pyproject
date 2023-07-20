''' This file contains the connection string to the MongoDB Atlas cluster. '''
import os
import sys
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck

def get_mongodb(database):
    ''' get the mongo db string '''
    print("[#] MongoDB Test Read data start")
    credid = credscheck('y:/pyproject/secrets/secrets.json')
    mongodbuser = credid["BotUsername"]
    mongodbpassword = credid["MongoPassword"]
    mongodbconnection = credid["MongoDatabase"]
    conn_str = f"mongodb+srv://{mongodbuser}:{mongodbpassword}@{mongodbconnection}/?retryWrites=true&w=majority"
    client = MongoClient(conn_str, server_api=ServerApi('1'))
    print("[#] MongoDB Test Read data start")
    return client[database]

def insertData(database, collection, datalist):
    ''' write mongodb data '''
    print("[=] MongoDB Test Insert data start")
    dbname = get_mongodb(database)
    collection_name = dbname[collection]
    collection_name.insert_many(datalist)
    print("[=] MongoDB Test Insert data end")

def readData(database, collection):
    ''' read mongodb data '''
    print("[=] MongoDB Test Read data start")
    dbname = get_mongodb(database)
    collection_name = dbname[collection]
    print("[=] MongoDB Test Read data Finish")
    return collection_name.find()

def main():
    ''' main function '''
    print("[-] MongoDB Test Main start")
    datalist = []
    datalist.append({   "_id" : "U1IT00009",   "item_name" : "new stuff",   "max_discount" : "10%",   "batch_number" : "RR450020FRG",   "price" : 30,   "category" : "stuff" })
    datalist.append({   "_id" : "U1IT00010",   "item_name" : "even more new Stuff",   "category" : "stuff",   "quantity" : 12,   "price" : 40,   "item_description" : "a bunch of stuff" })
    insertData('user_shopping_list', 'user_1_items', datalist)
    for item in readData('user_shopping_list', 'user_1_items'):
        print(item)

    print("[-] MongoDB Test Main end")

if __name__ == '__main__':
    print("[+] Starting MongoDB Test")
    main()
    print("[+] MongoDB Test Complete")
