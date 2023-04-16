'''
    this is a simple phone app for the DJ game
'''
import urllib.request
import pandas as pd
from pushbullet import Pushbullet
from djgamemodule import security as sec

def main():
    ''' this is the main routine'''
    credid = sec.credscheck('y:/pyproject/secrets/client_secrets.json')
    pb_access = credid["PushBullet_Key"]
    pb = Pushbullet(pb_access)
    all_pushes = pb.get_pushes()
    latest_push = all_pushes[0]
    url = latest_push['file_url']
    text_file = "phone.txt"
    urllib.request.urlretrieve(url, text_file)
    chat_list = []
    with open(text_file, "r", encoding='utf8') as f:
        data = f.readlines()
    final_data_set = data[1:]
    for line in final_data_set:
        date = line.split(",")[0]
        tim = line.split("-")[0].split(",")[1]
        name = line.split(":")[1].split("-")[1]
        message = line.split(":")[2][:-1]
        chat_list.append([date, tim, name, message])
    df = pd.DataFrame(chat_list, columns=["Date", "Time", "Name", "Message"])
    df.to_csv("phone.csv", index=False)

if __name__ == "__main__":
    main()
