'''This module is reponsible for manage the PersonList'''
import json
json_file = '../../json/mocked_person_list.json'

try:
    with open(json_file) as file:
        json_list = json.load(file)
except FileNotFoundError:
    print('test')
