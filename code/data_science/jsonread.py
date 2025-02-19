#!/usr/bin/env python
"""
a tool to read json
"""
import json
import requests

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

with open("Z:/Resources/development/data_file.json",
          "w",
          encoding='UTF8') as write_file:
    json.dump(data, write_file)

JSON_STRING = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data = json.loads(JSON_STRING)
print(data)

response = requests.get("https://jsonplaceholder.typicode.com/todos",
                        timeout=5)
todos = json.loads(response.text)

print(todos)
