'''This module only handle the PersonList and it's banch methods'''
from person import Person 

class PersonList():
    '''This class represent the 
    a list of Person classes'''

    def __init__(self, person_list:list[Person]): 
        '''PersonList construction's function'''
        self._check_construction_args(list)
        
        self.person_list = person_list

    def _check_construction_args(args: list[Person]):
        '''Validate arguments in the PersonList 
        construction function'''

        #Verify is the argument is a list
        if not isinstance(args, list):
            raise ValueError('A PersonList argument must be a list.')
        
        #Verify if every item of the list is a Person type
        if args:
            for arg in args:
                if not isinstance(arg, Person):
                    raise ValueError(f"Every value in the PersonList must be a " \
                    "a Person type - erro at {arg}")
