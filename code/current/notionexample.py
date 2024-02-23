'''
    a sample python notion integration
'''
import os
import sys
from datetime import datetime
from notion.client import NotionClient

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck # noqa: E402


def main():
    '''
        main function
    '''
    credid = credscheck('Z:/pyproject/secrets/secrets.json')
    notion_token = credid["Notion_Token"]
    notion_url = credid["Notion_Database"]
    # instantiate a client
    client = NotionClient(token_v2=notion_token)

    collection_view = client.get_collection_view(notion_url)
    new_row = collection_view.collection.add_row()
    new_row.Journaling = True
    new_row.Denis = True
    new_row.Running = True
    new_row.Screen_Time_Minutes = 30
    today = datetime.today()
    new_row.Title = today.strftime('%d.%m.%Y.%H.%M.%S')


if __name__ == "__main__":
    main()
