'''play.py '''


def main():
    ''' main '''
    print('[*] play.py main starting up')
    for i in range(10):
        print(f'[-] {i}')
        if i == 3:
            print('[-] 1 == 3')
            break
    else:
        print('[-] success')
    for j in range(10):
        print(f'[-] {j}')
        if i == 5:
            print('[-] 1 == 5')
            break
    else:
        print('[-] success')
    print('[*] play.py main shutting down')


if __name__ == "__main__":
    print('[+] play.py __main__ starting up')
    main()
    print('[+] play.py __main__ shutting down')
