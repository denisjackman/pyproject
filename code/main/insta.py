'''
    reddit and insta python script
'''
import os
import random
import json
from RedDownloader import RedDownloader
from instagrapi import Client


credentials = 'y:/pyproject/secrets/client_secrets.json'
with open(credentials, 'r', encoding='utf8') as f:
    creds = json.load(f)
username = creds['user_name']
password = creds['pass_word']


def GetMeme():
    '''
        get meme function
    '''
    post = RedDownloader.DownloadBySubreddit('dankmemes',
                                             1,
                                             output='meme',
                                             SortBy='new')
    authorname = post.GetPostAuthors()[0]
    return authorname


def GenerateCaption():
    '''
        generate insta caption
    '''
    captions = ['#pythoncoding #python #pythonprogramming #pythoncode #coding',
				'#programming #pythonlearning #pythondeveloper',
				'#pythonprogrammer #programmer #pythonprogramminglanguage',
				'#coder #pythonprojects #code #developer #codinglife #java',
				'#learnpython #datascience #machinelearning #codingbootcamp',
				'#computerscience #pythoncoder #codingisfun #programminglife',
				'#learncoding #programmingmemes #javascript #pythonlove',
				'#softwaredeveloper #learnprogramming #programmers #tech',
				'#artificialintelligence #programmerlife #learntocode',
				'#pythonsofinstagram #coderlife',
				'#softwareengineer #pycoders #codingmemes #technology',
				'#programmingisfun #pythonlanguage #coderslife #developerlife',
				'#codingfun #programmerslife #coders #programmerhumor',
				'#javaprogramming #ai #webdevelopment #programminglanguage',
				'#datascientist #codingforbeginners #codingproblems',
				'#codingtime #cprogramming #codingpics'
    ]
    return random.choice(captions)


def CleanUp():
    '''
        clean up function
    '''
    try:
        os.remove('meme/meme1.jpeg')
    except OSError as oserr:
        print(oserr)


client = Client()
client.login(username, password)

author = GetMeme()
hashtags = GenerateCaption()
caption = f'Credit to {author} \n {hashtags}'
try:
    client.photo_upload('meme/meme1.jpeg', caption)
except ClientError as err:
    print(err)
finally:
    print('Uploaded')

CleanUp()
