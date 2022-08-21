#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
info.py
https://python.plainenglish.io/how-to-get-location-information-of-an-ip-address-using-python-48c80ae98d59

"""
import requests

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.0 $"
__date__ = "$Date: 2022/09/21 00:31:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

def get_ip():
    '''
        get ip function
    '''
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_location(ip_address):
    '''
        get location function
    '''
    #ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data

def main():
    """ This is the main routine for the program """
    print(f"IP Address: {get_ip()}")
    print(f"IP Address: {get_location(get_ip())}")

if __name__ == '__main__':
    print("Starting the sequence:")
    main()
    print("finishing up and closing down:")
