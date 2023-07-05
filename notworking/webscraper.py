#!/usr/bin/env python
"""
This is a webscraper tool
"""
from bs4 import BeautifulSoup
import urllib3
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

urllib3.contrib.pyopenssl.inject_into_urllib3()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

WIKI = "https://en.WIKIpedia.org/WIKI/List_of_state_and_union_territory_capitals_in_India"

http = urllib3.PoolManager()
response = http.request('GET', WIKI)
SOUP = BeautifulSoup(response.data.decode('utf-8'))

print(SOUP.title)
print(SOUP.title.string)
print(SOUP.a)
