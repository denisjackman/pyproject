''' info from a mongo db '''
import os
import sys

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.dbfunctions.mongofunctions import open_mongo


def main():
    ''' main    '''
    print("[#] MongoDB Test start")
    mydb = open_mongo()
    print("[#] MongoDB Test done")
    for db_info in mydb.list_database_names():
        print(f"[-] DB Names are {db_info}")
        currentdb = mydb[db_info]
        collections = currentdb.list_collection_names()
        for collection in collections:
            print(f"[-] Collection Name is {collection}")


if __name__ == '__main__':
    print("[+] Starting MongoDB Test")
    main()
    print("[+] MongoDB Test Complete")
