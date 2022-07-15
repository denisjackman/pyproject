#!/usr/bin/env python
'''
    tokens
'''
import yaml

with open('items.yaml', 'r', encoding='utf8') as f:

    data = yaml.scan(f, Loader=yaml.FullLoader)

    for token in data:
        print(token)
