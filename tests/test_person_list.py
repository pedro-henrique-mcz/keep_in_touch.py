import unittest
from src.classes.person_list import PersonList
from src.classes.person import Person

class TestPersonList(unittest.TestCase):
    '''Test class for PersonList class'''
    def test_if_add_person_to_list_changes_the_list(self):
        '''This test garantee that the person add by
        the PersonList.add_person method will be in the last position 
        of the Person list in _people'''
        my_list = PersonList()
        my_person = Person('person_name')

        my_list.add_person(my_person)

        self.assertEqual(my_list._people[0], my_person)
        
