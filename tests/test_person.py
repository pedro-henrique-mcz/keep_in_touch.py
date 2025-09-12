import unittest
from src.classes.person import Person

class TestPerson(unittest.TestCase):

    def test_if_name_changes(self):
        '''Tests if the name changes propely'''
        my_person = Person('name')
        my_person.change_name('other_name')

        self.assertEqual(my_person.name,'other_name')


