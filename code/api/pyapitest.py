''' py api test
This script fetches a joke from an API and prints it.
the request is made to the API_URL and the response is printed.

the response is a json object.
It is checked if the response is successful and then the joke is printed.

The joke is contained in the json object as a setup and a delivery.


'''
import requests

API_URL = 'https://v2.jokeapi.dev/joke/Any'


def main():
    ''' main function '''
    response = requests.get(API_URL, timeout=5)
    if response.status_code != 200:
        print('Failed to fetch data:', response.status_code)
        return
    data = response.json()
    print(data["setup"])
    print(data["delivery"])


if __name__ == '__main__':
    main()
