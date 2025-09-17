'''This module are responsible for the Controller class'''
import json
import random
from datetime import datetime

from src.data.person import Person
from src.data.persons import Persons
from src.utils.utils_manager import open_json_file

class Controller():
    '''The Controller class is responsible for 
    manager the Persons class and select the person of the day'''

    def __init__(self, _json_file:str):
        
        # if not isinstance(_persons, Persons) or not _persons:
        #     raise ValueError(f'First argument must be a Persons type.')
        
        if not isinstance(_json_file, str) or not _json_file:
            raise ValueError(f'Second argument must be a String type.')
        
        self._json = _json_file
        self._data = open_json_file(_json_file) 

        self._date = datetime.strptime(self._data['sort_date'], "%Y-%m-%d")
        self._dict = self._data['person_list']
    

    def load_data(self):
        
        self._persons = Persons()

        for person in self._dict:
            self._persons.add_person(Person(person["name"], person["date"]))
        
    
    
        





       
        
    



