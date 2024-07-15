'''
    this gives you some details for a phone number
    pip install phonenumbers
'''
import phonenumbers
from phonenumbers import geocoder, carrier
__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.10 $"
__date__ = "$Date: 2022/08/18 08:31:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"


def check_number(number):
    """ this checks a number and returns a tuple of the results """
    try:
        number = phonenumbers.parse(number)
        provider = carrier.name_for_number(number, "en")
        region = geocoder.description_for_number(number, "en")
        return (True, number, provider, region)
    except phonenumbers.phonenumberutil.NumberParseException:
        return (False, None)


def main():
    """ This is the main routine for the program """
    print("Starting the sequence:")
    checkinput = input("Please enter a phone number with internation code: ")
    result = check_number(checkinput)
    print(result)
    print("finishing up and closing down:")


if __name__ == '__main__':
    main()
