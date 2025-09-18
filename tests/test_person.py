import unittest
import datetime 
import pytest
from src.data.person import Person

class TestPerson(unittest.TestCase):
    '''Test class for the Person Class'''

    def test_valid_args(self):
        '''tests if the args are valid or not in this 
        check function'''

        my_person = Person('Somenone', datetime.date(2000,6,27))

        valid_type = str
        my_type = 'string'

        self.assertEqual(
            my_person._valid_args(my_type, 'str', valid_type),
            True
        )

    def test_invalid_type(self):
        '''test case if s invalid type are throw'''
        my_person = Person('Somenone', datetime.date(2000,6,27))

        valid_type = str
        my_type = 2

        with pytest.raises(ValueError):
            my_person._valid_args(my_type, 'str', valid_type)

    def test_name_getter(self):
        '''Test the Person's name getter'''
        my_person = Person('Someone', datetime.date(2000,6,27))

        self.assertEqual(my_person.name(), 'Someone')
    
    def test_name_invalid_getter(self):
        '''Test the Person's invalid name getter'''
        my_person = Person('Someone', datetime.date(2000,6,27))

        with pytest.raises(ValueError):
            my_person.name(2)

    def test_valid_date_setter(self):
        '''Test a valid date setter for Person'''
        my_person = Person('Someone', datetime.date(2000,6,27))

        my_person.date(datetime.date(2002,7,5))

        self.assertEqual(my_person.date(), datetime.date(2002,7,5))

    def test_invalid_date_setter(self):
        '''Test a invalid Person's date change'''
        my_person = Person('Someone', datetime.date(2000,6,27))

        with pytest.raises(ValueError):
            my_person.date(2)