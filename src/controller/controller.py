'''This module is reponsible for manage the PersonList'''
from src.utils.utils_manager import open_json_file
import datetime
from src.data.persons import Persons
from src.data.person import Person
from src.data.controller import Controller

#opening the mocked persons, all paths are relative to main py in the root 
# json_file = 'json/mocked_person_list.json'
# data = open_json_file(json_file)

# people = Persons(data)

test = Person('Someone', datetime.date(2000,6,27))
print(test)

# my_controller = Controller( 'json/controller.json')
# my_controller.load_data()
# my_controller.shuffle()

