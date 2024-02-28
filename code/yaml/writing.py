#!/usr/bin/env python
'''
    writing yaml to a file
'''
import yaml

users = [{'name': 'John Doe', 'occupation': 'gardener'},
         {'name': 'Lucy Black', 'occupation': 'teacher'}]

with open('Z:/pyproject/resources/yaml/users.yaml',
          'w',
          encoding='utf-8-sig') as f:

    data = yaml.dump(users, f)
