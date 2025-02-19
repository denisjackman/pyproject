''' test mongo db connection '''
import os
import sys
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck


def main():
    ''' main function '''
    credid = credscheck('y:/pyproject/secrets/secrets.json')
    mongodbuser = credid["BotUsername"]
    mongodbpassword = credid["MongoPassword"]
    mongodbconnection = credid["MongoDatabase"]

    uri = "mongodb+srv://"\
          f"{mongodbuser}:{mongodbpassword}@{mongodbconnection}"\
          "/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
