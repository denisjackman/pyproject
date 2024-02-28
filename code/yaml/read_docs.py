#!/usr/bin/env python
'''
    read the yaml file
'''
import yaml

with open('Z:/pyproject/resources/yaml/data.yaml',
          'r',
          encoding='utf-8-sig') as f:

    docs = yaml.load_all(f, Loader=yaml.FullLoader)

    for doc in docs:

        for k, v in doc.items():
            print(k, "->", v)
