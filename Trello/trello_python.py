"""
trello_python.py
based on
https://owlcation.com/stem/Automated-To-Do-Lists-Creating-Boards-Lists-And-Cards-Using-Python-And-The-Trello-API

"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.10 $"
__date__ = "$Date: 2022/06/08 07:14:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"
import os
import sys
import requests

#pylint: disable=wrong-import-position
MODULE_PATH = "../module/"
sys.path.append(os.path.abspath(MODULE_PATH))
from jackmanimation import credscheck
#pylint: enable=wrong-import-position

cred_id = credscheck('../secrets/credentials.json')
key = cred_id["TrelloAPIKey"]
token = cred_id["TrelloToken"]


def create_board(board_name):
    """ create_board trello function """
    url = "https://api.trello.com/1/boards/"
    querystring = {"name": board_name, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    board_id = response.json()["shortUrl"].split("/")[-1].strip()
    return board_id


def create_list(board_id, list_name):
    """ create_list trello board function """
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    querystring = {"name": list_name, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    list_id = response.json()["id"]
    return list_id


def create_card(list_id, card_name):
    """ trello create card function """
    url = "https://api.trello.com/1/cards"
    querystring = {"name": card_name,
                   "idList": list_id,
                   "key": key,
                   "token": token}
    response = requests.request("POST", url, params=querystring)
    card_id = response.json()["id"]
    return card_id


def main():
    """ Main function here """
    board_id = create_board("Jackmanimation test")
    for filename in os.listdir():
        if filename.endswith(".txt"):
            filename = os.path.splitext(filename)[0]
            list_name = create_list(board_id, filename.title())
            with open(f"{filename}.txt", "r", encoding="utf8") as txt_file:
                for card_name in txt_file.readlines():
                    create_card(list_name, card_name)


if __name__ == '__main__':
    main()
