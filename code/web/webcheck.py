''' website status checker'''
import csv
import requests

status_dict = {"Website": "Status"}
INPUTFILE = "Z:/Resources/development/websites.txt"
OUTPUTFILE = "Z:/Resources/development/website_status.csv"


def website_check(webdebug=False):
    ''' website status checker '''
    if webdebug:
        print("[+] --- Start Website Check")
        print(f"[+] --- Input File is {INPUTFILE}")
        print(f"[+] --- Output File is {OUTPUTFILE}")
    with open(INPUTFILE, "r", encoding='utf-8-sig') as inputfile:
        for line in inputfile:
            website = line.strip()
            if webdebug:
                print(f"[+] --- Checking {website}")
            status = requests.get(website, timeout=5).status_code
            status_dict[website] = "working" if status == 200 \
                else "not working"
    if webdebug:
        print(f"[+] --- Output File is {OUTPUTFILE}")
        print(f"[+] --- Status Dict is {status_dict}")

    with open(OUTPUTFILE,
              "w",
              newline="",
              encoding='utf-8-sig') as outputfile:
        csv_writers = csv.writer(outputfile)
        for key, item in status_dict.items():
            csv_writers.writerow([key, item])

    if webdebug:
        print("[+] --- Website Check complete")


def main():
    ''' main function '''
    website_check()


if __name__ == '__main__':
    main()
