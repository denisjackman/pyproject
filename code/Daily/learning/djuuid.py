''' uuid example '''
from uuid import uuid4
import time


def main():
    ''' main function '''
    while True:
        time.sleep(0.1)
        print(uuid4(), end="\r")


if __name__ == "__main__":
    main()
