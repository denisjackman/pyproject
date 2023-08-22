''' djegg python script for the viscous case.'''
import crypt

def test_pass(cryptPass):
    ''' testPass function for the viscous case.'''
    salt = cryptPass[0:2]
    with open('dictionary.txt','r', encoding='utf-8-sig') as dictFile:
        for word in dictFile.readlines():
            word = word.strip('\n')
            cryptWord = crypt.crypt(word,salt)
            if cryptWord == cryptPass:
                print(f"[+] Found Password: {word}")
                return
    print("[-] Password Not Found.\n")
    return

def main():
    ''' main function for the viscous case.'''
    with open('passwords.txt','r', encoding='utf-8-sig') as passFile:
        for line in passFile.readlines():
            if ":" in line:
                user = line.split(':')[0]
                cryptPass = line.split(':')[1].strip(' ')
                print(f"[*] Cracking Password For: {user}")
                test_pass(cryptPass)

if __name__ == "__main__":
    main()
