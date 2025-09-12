'''This module is to hold the person class only'''

class Person():
    '''Person class'''
    def __init__(self, name):
        '''Person class construct name'''
        self.name = name
    
    def change_name(self, new_name):
        '''Person method to change name'''
        self.name = new_name



