'''whats app example '''
import time
import pywhatkit
import pyautogui
import keyboard


def main():
    ''' main function '''
    try:
        pywhatkit.sendwhatmsg_instantly('+447769836580', "hello python.", 10, tab_close=True)
        time.sleep(2)
        print("message sent")
        pyautogui.click()
        time.sleep(1)
        keyboard.press_and_release('enter')

    except Exception as err:
        print(f"error in sending {err}")


if __name__ == "__main__":
    main()
