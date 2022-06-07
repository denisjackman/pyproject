"""
    discord_bot.py
"""
import os
import sys

MODULE_PATH = "../module/"
sys.path.append(os.path.abspath(MODULE_PATH))
from jackmanimation import credscheck

import discord


def main():
    """ this is the main function """
    cred_id = credscheck()
    discord_token = cred_id["DiscordToken"]
    client = discord.Client()

    @client.event
    async def on_ready():
        print(
            f'{client.user} has connected to chat!\n'
            )

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content.startswith('$hello'):
            response = "Hello and welcome to the abyss!"
            await message.channel.send(response)

    client.run(discord_token)


if __name__ == '__main__':
    main()
