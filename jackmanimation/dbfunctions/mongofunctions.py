''' This file contains the connection string to the MongoDB Atlas cluster. '''
import os
import sys
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# pylint: disable=C0413
sys.path.append(os.path.realpath('..'))
from jackmanimation.gameitems.gamefunctions import credscheck


def open_mongo():
    ''' open mongo db '''
    dbdid = credscheck('y:/pyproject/secrets/secrets.json')
    mongodbuser = dbdid["BotUsername"]
    mongodbpassword = dbdid["MongoPassword"]
    mongodbconnection = dbdid["MongoDatabase"]
    conn_str = f"mongodb+srv://{mongodbuser}:{mongodbpassword}@{mongodbconnection}/?retryWrites=true&w=majority"
    client = MongoClient(conn_str, server_api=ServerApi('1'))
    return client


def get_mongodb(client, database):
    ''' get the mongo db string '''
    print("[#] MongoDB Test Read data start")
    print("[#] MongoDB Test Read data start")
    return client[database]


def insertData(client, database, collection, datalist):
    ''' write mongodb data '''
    print("[=] MongoDB Test Insert data start")
    dbname = get_mongodb(client, database)
    collection_name = dbname[collection]
    collection_name.insert_many(datalist)
    print("[=] MongoDB Test Insert data end")


def getData(client, database, collection):
    ''' read mongodb data '''
    print("[=] MongoDB Test Read data start")
    dbname = get_mongodb(client, database)
    collection_name = dbname[collection]
    print("[=] MongoDB Test Read data Finish")
    return collection_name.find()


def updateData(client, database, collection, itemid, field, value):
    ''' update mongodb data '''
    print("[=] MongoDB update data start")
    dbname = get_mongodb(client, database)
    collection_name = dbname[collection]
    update_result = collection_name.update_one({"_id": itemid}, {"$set": {field: value}})
    print("[=] MongoDB update data Finish")
    return update_result


def deleteData(client, database, collection, itemid):
    ''' delete mongodb data '''
    print("[=] MongoDB delete data start")
    dbname = get_mongodb(client, database)
    collection_name = dbname[collection]
    delete_result = collection_name.delete_one({"_id": itemid})
    print("[=] MongoDB delete data Finish")
    return delete_result


def main():
    ''' main function '''
    print("[-] MongoDB Test Main start")
    print("[-] MongoDB Test Main end")


if __name__ == '__main__':
    main()
