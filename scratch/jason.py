'''
    This is jason an alexa type tool in python

    Modules:
    pip install pyttsx3
    pip install speechrecognition
    pip install pywhatkit
    pip install wikipedia
    pip install pyjokes

    reference:
    https://plainenglish.io/blog/build-your-own-alexa-with-just-20-lines-of-python-ea8474cbaab7
    https://content.techgig.com/technology-guide/code-up-build-your-own-alexa-in-just-6-steps-by-using-python/articleshow/87734466.cms

'''

import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes

DEBUG_FLAG = False
LISTENER = sr.Recognizer()
ENGINE = pyttsx3.init()
VOICES = ENGINE.getProperty('voices')
ENGINE.setProperty('voice',VOICES[1].id)

def talk(text):
    ''' this is the talk module '''
    ENGINE.say(text)
    ENGINE.runAndWait()
    if DEBUG_FLAG:
        print(f'OUTPUT : {text}')

def command(localcommand):
    ''' this is the command module '''
    if DEBUG_FLAG:
        print(f'INPUT : {localcommand}')

def statup_sequence():
    ''' this is the statup sequence '''
    talk("Hello, I am jason")
    talk("reactor online")
    talk("sensors online")
    talk("weapons online")
    talk("all systems nominal")  
    
def main():
    ''' main function '''
    statup_sequence()

if __name__ == '__main__':
    main()
