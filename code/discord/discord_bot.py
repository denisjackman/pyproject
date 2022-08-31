#!/usr/bin/python
"""
    discord_bot.py
"""
import discord
from djgamemodule import security as sec

VERSION = "01.00 Alpha (Sugar)"


def main():
    """ this is the main function """
    cred_id = sec.credscheck('../secrets/credentials.json')
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
            response = r"""

        Hello and I am the jackmanimation bot!
            my commands are:
            - **$help** - this command
            - **$hello** - a greeting command
            - **$about** - more about the discord bot
            - **$version** - the version information for the bot
        More commands are being added daily

            """
            await message.channel.send(response)
        if command.startswith('$about'):
            response = r"""
Jackmanimation Discord Bot
            Developed by : **Denis Jackman**
            Official Website : https://github.com/denisjackman/pyproject
            Copyright : **2022**
            """
            await message.channel.send(response)
        if command.startswith('$hello'):
            response = "Hello and welcome to the abyss!"
            await message.channel.send(response)

        if command.startswith('$version'):
            response = "Jackmanimation Bot : [Version : **" + VERSION + "**]"
            await message.channel.send(response)

    client.run(discord_token)


if __name__ == '__main__':
    main()
