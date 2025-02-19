'''
    a python script to control the mouse and keyboard
    Links:
        https://python.plainenglish.io/python-script-that-kept-me-online-all-day-2957c62ec44d
        https://automatetheboringstuff.com/2e/chapter20/
'''
import pyautogui


def main():
    ''' main function '''
    # move the mouse to the center of the screen
    pyautogui.moveTo(960, 540, duration=1)
    # click the mouse
    pyautogui.click()
    # type some text
    pyautogui.typewrite('Hello world!', interval=0.25)
    # press the enter key
    pyautogui.press('enter')


if __name__ == '__main__':
    main()
