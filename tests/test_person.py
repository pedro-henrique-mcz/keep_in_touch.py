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


    