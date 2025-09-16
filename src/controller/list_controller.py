'''This module is reponsible for manage the PersonList'''
from src.utils.utils_manager import open_json_file

json_file = 'json/mocked_person_list.json'
data = open_json_file(json_file)

print(data)
