'''This module is reponsible for manage the PersonList'''
from src.utils.utils_manager import open_json_file
from src.data.persons import PersonList
from src.data.person import Person

#opening the mocked persons, all paths are relative to main py in the root 
json_file = 'json/mocked_person_list.json'
data = open_json_file(json_file)

def transform_into_personlist(persons:list) -> PersonList:
    person_list = PersonList
    
    for person in persons:
        if isinstance(person, str) and person:
            person_list.add_person(Person(person.lower()))

    return PersonList

