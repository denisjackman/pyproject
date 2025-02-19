''' Threading example in python '''
import threading
import time


def print_numbers():
    ''' print numbers '''
    for i in range(1, 11):
        print(f'[-] number function - {i}')
        time.sleep(0.5)


def print_letters():
    ''' print letters '''
    for item in "abcdefghij":
        print(f'[-] letter function - {item}')
        time.sleep(0.5)


def main():
    ''' main function '''
    print("[+] -- Main Function Start")
    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_letters)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("[+] -- Main Function End")


if __name__ == "__main__":
    main()
