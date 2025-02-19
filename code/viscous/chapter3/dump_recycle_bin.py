''' checking the recycle bin '''
import os
import platform
import ctypes

RUN_NAME = os.path.basename(__file__)
OS_NAME = platform.system()
RUN_CHECK = False
IS_ADMIN = ctypes.windll.shell32.IsUserAnAdmin() != 0

if OS_NAME == 'Windows':
    import winreg  # pylint: disable=E0401
    RUN_CHECK = True


def sid2user(sid):
    ''' convert SID to username '''
    targetdir = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\\"
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,  # pylint: disable=E0606
                             f'{targetdir}{sid}')
        (value, _) = winreg.QueryValueEx(key, 'ProfileImagePath')
        user = value.split('\\')[-1]
        return user
    except WindowsError:  # pylint: disable=E0602
        return sid


def return_dir():
    ''' return recycle bin directory '''
    dirs = ['C:\\Recycler\\',
            'C:\\Recycled\\',
            'C:\\$Recycle.Bin\\']
    for recycle_dir in dirs:
        if os.path.isdir(recycle_dir):
            return recycle_dir
    return None


def find_recycled(recycle_dir):
    ''' find files in recycle bin '''
    dir_list = os.listdir(recycle_dir)
    for sid in dir_list:
        files = os.listdir(recycle_dir + sid)
        user = sid2user(sid)
        print(f'[*] Listing Files For User: {str(user)}')
        for file in files:
            print(f'[+] Found File: {str(file)}')


def main():
    ''' main '''
    recycle_dir = return_dir()
    find_recycled(recycle_dir)


if __name__ == '__main__':
    print(f'[-] {RUN_NAME} starting')
    if RUN_CHECK:
        if IS_ADMIN:
            main()
        else:
            print(f'[-] {RUN_NAME} requires elevated privileges')
    else:
        print(f'[-] {OS_NAME} not supported')
    print(f'[-] {RUN_NAME} complete')
