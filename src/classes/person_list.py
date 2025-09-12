'''This module only handle the PersonList and it's banch methods'''
from .person import Person 

class PersonList():
    '''This class represent the 
    a list of Person classes'''

    def __init__(self, person_list:list[Person]): 
        '''PersonList construction's function'''
        self.person_list = person_list

  