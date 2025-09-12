'''This module only handle the PersonList and it's banch methods'''
from .person import Person 

class PersonList():
    '''This class represent the 
    a list of Person classes'''

    def __init__(self, _people:list[Person]=[]): 
        '''PersonList construction's function'''
        
        #if no list of person is placed, 
        # the default parameter will be a empty list
        self._people = _people

    def add_person(self, person:Person) -> Person:
        '''Simple adding of a person into the PersonList'''
        self._people.append(person)
        return person

    def remove_person(self, name:str):
        '''Simple revome method for remove
        some person from the list of PersonList'''
        person = 
    
    def search_person(self, name:str) -> tuple|None:
        '''This function return some person 
        from the PersonList'''

        for person, index in self._people:
            if person.name == name:
                return (person, index)
            
        return None

