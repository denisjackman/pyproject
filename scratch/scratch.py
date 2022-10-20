'''
    this is a scratch python file
'''
import subprocess

def main():
    '''
        this is the main function
    '''
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
    data = meta_data.decode('utf-8', errors='backslashreplace').split('\n')
    profiles = []
    for item in data:
        if 'All User Profile' in item:
            profiles.append(item.split(':')[1].strip())
    print('Wi-fi Name : Password')
    print('---------------------')
    for result in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', result, 'key=clear']).decode('utf-8').split('\n')
            results = [item.split(':')[1].strip() for item in results if 'Key Content' in item]
            try:
                print(f'{result} : {results[0]}')
            except IndexError:
                print(f'{result} : Password not found')
        except subprocess.CalledProcessError:
            print(f'{result} : Error Occured')

if __name__ == "__main__":
    main()
