"""
    discord_bot.py
"""
import discord
from jackmanimation import credscheck


def main():
    """ this is the main function """
    cred_id = credscheck()
    discord_token = cred_id["DiscordToken"]
    discord_guild = cred_id["DiscordGuildname"]
    client = discord.Client()

    @client.event
    async def on_ready():
        guild = None
        for guild in client.guilds:
            if guild.name == discord_guild:
                break

        print(
            f'{client.user} has connected to the following guild:\n'
            f'{guild.name}(ID: {guild.id})'
            )

        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')

    client.run(discord_token)


if __name__ == '__main__':
    main()
