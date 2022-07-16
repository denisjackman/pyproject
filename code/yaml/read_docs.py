#!/usr/bin/env python
'''
    read the yaml file
'''
import yaml
with open('y:/pyproject/resources/yaml/data.yaml', 'r', encoding='utf8') as f:

    docs = yaml.load_all(f, Loader=yaml.FullLoader)

    for doc in docs:

        for k, v in doc.items():
            print(k, "->", v)
