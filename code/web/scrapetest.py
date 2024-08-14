'''
    web scraper
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
FIRST_URL = "http://www.pythonscraping.com/pages/page1.html"
OTHER_URL = "https://www.yelp.com/biz/milk-and-cream-cereal-bar-new-york?osq=Ice+Cream"
with urlopen(OTHER_URL) as html:
    bsObj = BeautifulSoup(html.read(), 'html.parser')
print(bsObj.prettify())
