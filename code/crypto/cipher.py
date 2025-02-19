# Caesar Cipher
"""
 This is a cipher script
"""
MAX_KEY_SIZE = 26


def get_mode():
    """
    get_mode Function
    """
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        smode = input().lower()
        if smode in 'encrypt e decrypt d'.split():
            return smode
        print('Enter either "encrypt" or "e" or "decrypt" or "d".')


def get_message():
    """
    get_message Function
    """
    print('Enter your message:')
    return input()


def get_key():
    """
    get_key Function
    """
    skey = 0
    while True:
        print(f'Enter the KEY number ({MAX_KEY_SIZE})')
        skey = int(input())
        # if (skey >= 1 and skey <= MAX_KEY_SIZE):
        #    return skey
        if 1 <= skey <= MAX_KEY_SIZE:
            return skey


def get_translated_message(amode, amessage, akey):
    """
    getTranslateMessage Function
    """
    if amode[0] == 'd':
        akey = -akey
    translated = ''

    for symbol in amessage:
        if symbol.isalpha():
            num = ord(symbol)
            num += akey

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated


mode = get_mode()
message = get_message()
KEY = get_key()
codePack = chr(KEY+65)+get_translated_message(mode, message, KEY)
emessage = get_translated_message(mode, message, KEY)
print(f'Your translated text is: {message}  : {emessage}')
