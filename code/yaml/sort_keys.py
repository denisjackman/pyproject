#!/usr/bin/env python
'''
    sorting keys
'''
import yaml

with open('y:/pyproject/resources/yaml/items.yaml', 'r', encoding='utf8') as f:

    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)

    yaml_sorted = yaml.dump(data, sort_keys=True)
    print(yaml_sorted)
