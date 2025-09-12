'''This module is to hold the person class only'''

class Person():
    '''Person class'''
    def __init__(self, name):
        '''Person class construct name'''
        self._validation_name(name)
        self.name = name
    
    def change_name(self, new_name):
        '''Person method to change name'''
        self._validation_name(new_name)
        self.name = new_name

    def _validation_name(self, name):
        '''Name validation'''
        if not isinstance(name, str) or not name.strip():
            raise ValueError("The person's name must be a " \
            "string and cannot to be empty.")
        

