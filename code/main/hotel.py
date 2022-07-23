'''
    Hotel API call
'''
import requests

url = "https://hotels4.p.rapidapi.com/locations/v2/search"

querystring = {"query": "london", "locale": "en_GB", "currency": "GBP"}

headers = {
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com",
    "X-RapidAPI-Key": "d559163cd2mshb5c848c6070fbd8p1bf345jsn3b29fdb230fe"
}

response = requests.request("GET", url, headers=headers, params=querystring)
print(type(response))
# print(response.data)
