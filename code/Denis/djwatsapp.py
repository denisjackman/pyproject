'''whats app example '''
import pywhatkit


def main():
    ''' main function '''
    try:
        pywhatkit.sendwhatmsg_instantly('+447769836580', "hello python.", 10, tab_close=True)
        print("message sent")
    except Exception as err:
        print(f"error in sending {err}")


if __name__ == "__main__":
    main()
