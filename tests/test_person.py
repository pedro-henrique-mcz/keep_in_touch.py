import unittest
import datetime 
import pytest
from src.data.person import Person

class TestPerson(unittest.TestCase):
    '''Test class for the Person Class'''

    def test_invalid_name(self):
        '''Tests invalid types name.'''

        invalid_types = [
            123,
            ("a", "b"),
            3.14,
            [],
            None,
            True,
            {"key": "value"}
        ]

        with pytest.raises(ValueError):
            for arg in invalid_types:
                Person(arg , datetime.date(2000,6,27))

    def test_invalid_date(self):
    
        '''Tests invalid date types.'''

        invalid_types = [
            123,
            ("a", "b"),
            3.14,
            [],
            None,
            True,
            {"key": "value"},
            "string"
        ]

        with pytest.raises(ValueError):
            for arg in invalid_types:
                Person("Someone", arg)
    
        
    def test_str(self):
        '''Tests the return of __str__'''
        my_person = Person('Someone', datetime.date(2000,6,27))
        self.assertEqual(print(my_person), f'name={my_person._name}, date={my_person._date}')

