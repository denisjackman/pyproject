'''
using telegram bot to send messages to users

    using the work in code/telgrambot/telgrambot.py to send messages to users
    using the work in code/tkproject/encbuilder.py to build the function
    using the work in code/tkproject/maturam.py to build the function
'''
MATURAM_DEBUG = True
MATURAM_LOG = True
MATURAM_LOG_FILE = "maturam.log"


def log(log_message):
    '''log function for the program'''
    if MATURAM_DEBUG:
        print(log_message)
        if MATURAM_LOG:
            with open(MATURAM_LOG_FILE,
                      'a',
                      encoding='utf-8-sig') as log_file:
                log_file.write(log_message)
                log_file.write('\n')


def main():
    '''main function of the program'''
    log("[-] Maturam is starting")
    log("[-] Maturam is ending")


if __name__ == "__main__":
    main()
