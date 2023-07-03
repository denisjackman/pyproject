#!/usr/bin/env python
'''
    yaml within python
'''

import yaml

with open('y:/pyproject/resources/yaml/items.yaml','r',encoding='utf-8-sig') as f:

    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
