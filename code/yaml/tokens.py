#!/usr/bin/env python
'''
    tokens
'''
import yaml

with open('Z:/pyproject/resources/yaml/items.yaml',
          'r',
          encoding='utf-8-sig') as f:

    data = yaml.scan(f, Loader=yaml.FullLoader)

    for token in data:
        print(token)
