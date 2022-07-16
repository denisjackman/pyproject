#!/usr/bin/env python
'''
    writing yaml to a file
'''
import yaml

users = [{'name': 'John Doe', 'occupation': 'gardener'},
         {'name': 'Lucy Black', 'occupation': 'teacher'}]

with open('y:/pyproject/resources/yaml/users.yaml', 'w', encoding='utf8') as f:

    data = yaml.dump(users, f)
