"""
    discord_bot.py
"""
import os
import sys
#pylint: disable=wrong-import-position
MODULE_PATH = "../module/"
sys.path.append(os.path.abspath(MODULE_PATH))
from jackmanimation import credscheck
#pylint: enable=wrong-import-position
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
        # convert the message into a string
        # this allows us to turn into lower case
        command = message.content
        command = command.lower()
        if command.startswith('$help'):
            #pylint: disable=line-too-long
            response = "Hello and the jackmanimation bot!\nmy commands are:\n $help - this command \n$hello - a greeting command"
            #pylint: enable=line-too-long
            await message.channel.send(response)

        if command.startswith('$hello'):
            response = "Hello and welcome to the abyss!"
            await message.channel.send(response)

    client.run(discord_token)


if __name__ == '__main__':
    main()
