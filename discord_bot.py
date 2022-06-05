"""
    discord_bot.py
"""
from jackmanimation import credscheck
import discord


def main():
    """ this is the main function """
    cred_id = credscheck()
    TOKEN = cred_id["DiscordToken"]
    GUILD = cred_id["DiscordGuildname"]
    client = discord.Client()

    @client.event
    async def on_ready():
        for guild in client.guilds:
            if guild.name == GUILD:
                break

        print(
            f'{client.user} has connected to the following guild:\n'
            f'{guild.name}(ID: {guild.id})'
            )

        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')

    client.run(TOKEN)


if __name__ == '__main__':
    main()
