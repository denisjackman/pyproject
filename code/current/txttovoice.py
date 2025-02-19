''' text to voice '''
import pyttsx3


def main():
    ''' Main function '''
    text = 'Hello, world!'
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    main()
