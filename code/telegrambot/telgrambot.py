'''
Maturam Bot
This is the skelton for a telgram bot

TODO:
1 - take the code in the maturm function and load it into the bot
2 - create a function that will take the message and return the response
3 - create a function that will take the response and send it back to the user
4 - create a function that will take the response and send it to the channel
5 - use the DND actions to generate items as needed

'''
import sys
import os
import telebot

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck

BOT_NAME = "Maturam"
BOT_USERNAME = "jackmanimationbot"
SECRETS = "Z:/pyproject/secrets/secrets.json"
BOT_DEBUG = True
BOT_MESSAGE = f'Welcome to {BOT_NAME} channel. I am {BOT_USERNAME}.'
BOT_RUNNING = True


def bot_setup():
    '''setup the bot'''
    if BOT_DEBUG:
        print("[-] Bot_Setup is starting")
    bs_credid = credscheck(SECRETS)
    bs_bot_token = bs_credid["telegram_token"]
    bs_bot = telebot.TeleBot(bs_bot_token)
    if BOT_DEBUG:
        print("[-] Bot_Setup is ending")
    return bs_bot


def bot_message(bm_bot):
    '''bot message function'''
    @bm_bot.message_handler(commands=['start', 'help', 'about', 'quit'])
    def send_welcome(message):
        bm_bot.reply_to(message, BOT_MESSAGE)
        if message.text.lower() == '/quit':
            bm_bot.reply_to(message, "[-] TelegramBot is ending")
            bm_bot.stop_polling()


def bot_reply(br_bot):
    '''bot reply function'''
    @br_bot.message_handler(func=lambda message: True)
    def echo_all(message):
        br_bot.reply_to(message, message.text)


def main():
    '''main function of the program'''
    print("[-] TelegramBot is starting")
    main_bot = bot_setup()
    bot_message(main_bot)
    bot_reply(main_bot)
    main_bot.infinity_polling()
    print("[-] TelegramBot has ended")


if __name__ == "__main__":
    main()
