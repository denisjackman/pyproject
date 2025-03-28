import requests
api_url = 'https://api.api-ninjas.com/v1/quotes'
response = requests.get(api_url, headers={'X-Api-Key': 'KbDwuYgWSvSEdfRQP5HIRA==c7XvWOkDEcZb6sNu'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)
    