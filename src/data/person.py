'''This module is to hold the person class only'''

class Person():
    '''Person class'''
    def __init__(self, name):
        '''Person class construct name'''
        self.name = name
    
    def change_name(self, new_name):
        '''Person method to change name'''
        self.name = new_name

    def __eq__(self, other):
        '''This fuction allow us to 
        verify is two persons are the same in boolean 
        tests'''
        if not isinstance(other, Person):
            return NotImplemented
        return self.name == other.name


