'''Test for the PersonList class'''
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
    
    def test_the_person_added_is_the_person_returned(self):
        '''This tests if the person that was added before
        is the same person that will be returned
        in the end of the add_person function'''
        my_list = PersonList()
        person_input = Person('person_name')

        person_added = my_list.add_person(person_input)

        self.assertEqual(person_input, person_added)

        
    def test_if_search_person_return_person(self):
        '''Tests if the search_person method find
        and return the a person by name'''
        name = 'person_name'
        
        my_person = Person(name)
        my_list = PersonList([my_person])
        
        person_finded = my_list.search_person(name)
        self.assertEqual(my_person, person_finded)

        
    def test_if_search_person_return_none(self):
        '''Test if the search_person method fails and 
        return none if it dosen't find the person in
        the list'''

        name = 'person_name'
        other_name = "unknow_name"
        
        my_person = Person(name)
        my_list = PersonList([my_person])
        
        person_finded = my_list.search_person(other_name)
        self.assertEqual(None, person_finded)