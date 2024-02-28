#!/usr/bin/env python
'''
    sorting keys
'''
import yaml

with open('Z:/pyproject/resources/yaml/items.yaml',
          'r',
          encoding='utf-8-sig') as f:

    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)

    yaml_sorted = yaml.dump(data, sort_keys=True)
    print(yaml_sorted)
