'''This module only handle the PersonList and it's banch methods'''
from .person import Person 

class Persons():
    '''This class represent the 
    a list of Person classes'''

    def __init__(self, _list:list=[]): 
        '''PersonList construction's function'''
        
        #if no list of person is placed, 
        # the default parameter will be a empty list
        self._people = []

        if not isinstance(_list, list) and list:
            raise ValueError('Persons argument must be a list type.')

        for people in _list:
            if isinstance(people, str) and people:
                self._people.append(Person(people))
            else:
                raise ValueError('All items of the list must to be string type.')
            
            

    def add_person(self, person:Person) -> Person:
        '''Simple adding of a person into the PersonList'''
        self._people.append(person)
        return person

    def remove_person(self, name:str) -> bool:
        '''Simple revome method for remove
        some person from the list of PersonList'''
        index = self.search_person(name)
        self._people.remove(self._people[index]) 
        
        return True    

    def show_all(self) -> list[Person]:
        return self._people

    def search_person(self, name:str) -> int|None:
        '''This function return some person 
        from the PersonList'''

        for i in range(len(self._people)):
            if self._people[i].name == name:
                return i
            
        return None

