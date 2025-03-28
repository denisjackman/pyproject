
"""
xavidiscord.py

This is for a discord bot
For the bot:

https://discordpy.readthedocs.io

For reading from Excel:

https://pypi.org/project/openpyxl/

(Although I would recommend using pretty much any other data source instead of using Excel)

"""
import os
import sys
import random
import json
import requests
import discord
from dockermysqlex import get_secrets

sys.path.append(os.path.realpath('../..'))

maincredid = get_secrets('../../secrets/nusecrets.json')

QUOTES_API= "https://api.api-ninjas.com/v1/quotes"

TOKEN = maincredid["discordbottoken"]
QUOTES_API_KEY = maincredid["ninjaapikey"]

discordclient = discord.Client(intents=discord.Intents.default())

ADMIN_CHANNEL = 984372901950132226
BOTTEST_CHANNEL = 984373002030415872
GENERAL_CHANNEL = 984373076923936799
PROJECTS_CHANNEL = 989439933137702972


def get_qoute():
    ''' gets a quote'''
    gq_quote = None
    gq_api_url = QUOTES_API
    gq_response = requests.get(gq_api_url, headers={'X-Api-Key': QUOTES_API_KEY}, timeout=5)
    if gq_response.status_code == requests.codes.ok:
        gq_json_data = json.loads(gq_response.text)
        gq_quote = f"{gq_json_data[0]['quote']} - {gq_json_data[0]['author']}"
    else:
        gq_quote = f"Error: {gq_response.status_code}, {gq_response.text}"
    return gq_quote


@discordclient.event
async def on_ready():
    ''' discord '''
    print(f'{discordclient.user} has connected to Discord!')


@discordclient.event
async def on_member_join(member):
    ''' on member join '''
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@discordclient.event
async def on_message(message):
    ''' on-message '''
    if message.author == discordclient.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    response = None
    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)

    if message.content.lower() == '!version':
        response = "Frankie bot - 2025 - version Alpha - 20250320"

    if message.content.lower() == '!inspire':
        response = get_qoute()

    if response is not None:
        await message.channel.send(response)


if __name__ == '__main__':
    discordclient.run(TOKEN)
