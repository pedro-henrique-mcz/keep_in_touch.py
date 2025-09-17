'''This module is to hold the person class only'''
import datetime

class Person():
    '''Person class'''
    def __init__(self, name:str, date:datetime.date):
        '''Person class construct'''

        if not isinstance(name, str) or not name:
            message = 'The "name" argument in Person Object must be a str type.'
            
            raise ValueError(message)
        
        if not isinstance(date, datetime.date) or not date:
            message = 'The "date" argument in Person Object ' \
            'must be a datetime.date type.'
            
            raise ValueError(message)

        self._name = name
        self._date = date
    
    def name(self) -> str:
        '''Person name handler'''
        return self._name

    def date(self) -> datetime.date:
        '''Person date handler'''
        return self._date

    def __str__(self):
        '''String representation for debugs'''
        return f'name={self._name}, date={self._date}'


