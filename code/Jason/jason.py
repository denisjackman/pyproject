'''
    This is jason an alexa type tool in python

    Modules:
    pip install pyttsx3
    pip install speechrecognition
    pip install pywhatkit
    pip install wikipedia
    pip install pyjokes
    pip install pyaudio
    pip install numpy
    pip install sounddevice
    pip install soundfile

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
import sounddevice as sd
import soundfile as sf

DEBUG_FLAG = False
LISTENER = sr.Recognizer()
LISTENER.energy_threshold = 4000
ENGINE = pyttsx3.init()
VOICES = ENGINE.getProperty('voices')
ENGINE.setProperty('voice', VOICES[0].id)


def talk(text):
    ''' this is the talk module '''
    ENGINE.say(text)
    ENGINE.runAndWait()
    if DEBUG_FLAG:
        print(f'OUTPUT : {text}')


def googlesearch(searchterm):
    ''' this is the watsapp module '''
    pywhatkit.search(searchterm)
    talk(f"Search for {searchterm} complete")


def listen():
    ''' this is the listen module '''
    listencommand = 'not found'
    try:
        with sr.Microphone() as listensource:
            print('Listening...')
            listenvoice = LISTENER.listen(listensource)
            listencommand = LISTENER.recognize_google(listenvoice)
            listencommand = listencommand.lower()
            if DEBUG_FLAG:
                print(f'INPUT : {listencommand}')
    except Exception as djerror:  # pylint: disable=bare-except
        print(f"Error: {djerror} {type(djerror)} {djerror.args}")

    return listencommand


def wiki(search):
    ''' this is the wiki module '''
    info = wikipedia.summary(search, 1)
    print(info)
    talk(info)


def jasontime():
    ''' this is the time module '''
    ytime = datetime.datetime.now().strftime('%I:%M %p')
    talk('Current time is ' + ytime)
    print(ytime)


def command(localcommand):
    ''' this is the command module '''
    if DEBUG_FLAG:
        print(f'INPUT : {localcommand}')


def startup_sequence():
    ''' this is the statup sequence '''
    talk("Hello, I am jason")
    talk("reactor online")
    talk("sensors online")
    talk("weapons online")
    talk("all systems nominal")


def systemscheck():
    ''' check function '''
    checkfile = 'Z:/Resources/sounds/reactor.wav'
    data, fs = sf.read(checkfile, dtype='float32')
    sd.play(data, fs)
    status = sd.wait()
    print(f"status: {status}")


def joke():
    ''' joke function '''
    tempjoke = pyjokes.get_joke()
    print(f"{tempjoke}")
    talk(tempjoke)


def video(videotext):
    ''' this is the video module '''
    messagetext = f"Playing {videotext}"
    try:
        pywhatkit.playonyt(videotext)
        messagetext = f"playing {videotext}"
    except Exception as djerror:  # pylint: disable=bare-except
        messagetext = f"Error: {djerror} "\
                      f"{type(djerror)} "\
                      f"{djerror.args} for "\
                      f"{videotext}"
    print(messagetext)
    talk(messagetext)


def main():
    ''' main function '''
    JasonRunning = True
    while JasonRunning:
        jasoncommand = listen()
        print(f"command: {jasoncommand}")
        if 'play' in jasoncommand:
            jasoncommand = jasoncommand.replace('play', '')
            video(jasoncommand)
        elif 'search' in jasoncommand:
            jasoncommand = jasoncommand.replace('search', '')
            googlesearch(jasoncommand)
        elif 'time' in jasoncommand:
            jasontime()
        elif 'joke' in jasoncommand:
            joke()
        elif 'stop' in jasoncommand:
            JasonRunning = False
            talk("Goodbye")
        elif 'check' in jasoncommand:
            systemscheck()
            talk("Systems check complete")
        else:
            talk("I did not understand that")
    print("done")


if __name__ == '__main__':
    main()
