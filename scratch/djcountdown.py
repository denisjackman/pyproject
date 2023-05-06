''' This is a simple countdown timer that takes a user input in seconds and counts down to zero.'''
import time

def countdown(timecount, timeverb= False):
    '''This function takes a user input in seconds and counts down to zero.'''
    while timecount:
        mins, secs = divmod(timecount, 60)
        timer = f'{mins:02d}:{secs:02d}'
        if timeverb:
            print(f"{timer}\r")
        time.sleep(1)
        timecount -= 1
    if timeverb:
        print('Timer completed!')

def main():
    ''' main function '''
    countdown(10, True)
    countdown(5, False)

if __name__ == '__main__':
    main()
