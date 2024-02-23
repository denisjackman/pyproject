'''
    example scraping script
'''
import re
import json
import requests

URL = "https://nonolive.com/45316761"

html_doc = requests.get(URL, timeout=5).text
data = re.search(r"window\.__INITIAL_STATE__=(.*?);", html_doc).group(1)
data = json.loads(data)

# pretty print the data:
print(json.dumps(data, indent=4))
