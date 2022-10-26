'''
    a sample python notion integration
'''
from datetime import datetime
from notion.client import NotionClient
from djgamemodule import security as sec

def main():
    '''
        main function
    '''
    credid = sec.credscheck('y:/pyproject/secrets/credentials.json')
    notion_token = credid["Notion_Token"]
    notion_url = credid["Notion_Database"]
    notion_page = credid["Notion_Page"]
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
    #new_collection_view = client.get_collection_view(notion_page)
    #new_text = new_collection_view.collection.name = "Programming Test"

    # get the page
    #page = client.get_block(notion_url)

    # print the title
    #print(page.title)

if __name__ == "__main__":
    main()
