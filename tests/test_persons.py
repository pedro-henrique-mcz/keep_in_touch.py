# '''Test for the PersonList class'''
# import unittest
# import pytest
# from src.data.persons import Persons
# from src.data.person import Person


# class TestPersons(unittest.TestCase):
#     '''Test class for Persons class'''

#     def test_persons_valid_args(self):
#         '''this will teste if person return every single item 
#         from a list full of acceptable itens'''
#         my_list = ['Pedro', 'Antônio', 'Edriana', 'Álvaro']
#         my_persons = Persons(my_list)

#         my_persons_clone = [
#             Person('Pedro'),
#             Person('Antônio'),
#             Person('Edriana'),
#             Person('Álvaro')
#         ]

#         for i in range(len(my_list)):
#             self.assertEqual(my_persons._people[i], my_persons_clone[i])

#     def test_persons_with_invalid_argument(self):
#         '''Tests if the persons class will raise a error
#         if the wrong argument goes '''
#         invalid_argument = [
#         123,
#         ("a", "b"),
#         3.14,
#         "uma string",
#         None,
#         True,
#         {"key": "value"}
#         ]

#         with pytest.raises(ValueError):
#             for argument in invalid_argument:
#                 Persons(argument)

#     def test_list_with_no_str_and_void_items(self):
#         '''Tests Persons constructo with a list with no 
#         str itens within'''
#         my_list = [
#             'Pedro', 
#             8, 
#             'Antônio', 
#             {'nome':'Edriana'}, 
#             [], 
#             'Álvaro', 
#             None
#         ]
        
#         valid_itens = [
#             Person('Pedro'),
#             Person('Antônio'),
#             Person('Álvaro')
#         ]

#         my_persons = Persons(my_list).show_all()
        
#         for i in range(len(my_persons)):
#             self.assertEqual(my_persons[i], valid_itens[i]) 


#     def test_if_add_person_to_list_changes_the_list(self):
#         '''This test garantee that the person add by
#         the Persons.add_person method will be in the last position 
#         of the Person list in _people'''
#         my_list = Persons()
#         my_person = Person('person_name')

#         my_list.add_person(my_person)

#         self.assertEqual(my_list._people[0], my_person)
    
#     def test_the_person_added_is_the_person_returned(self):
#         '''This tests if the person that was added before
#         is the same person that will be returned
#         in the end of the add_person function'''
#         my_list = Persons()
#         person_input = Person('person_name')

#         person_added = my_list.add_person(person_input)

#         self.assertEqual(person_input, person_added)

        
#     def test_if_search_person_return_person(self):
#         '''Tests if the search_person method find
#         and return the a person by name'''
#         name = 'person_name'
#         my_list = Persons([name])
#         index = my_list.search_person(name)

#         self.assertEqual(my_list._people[0], my_list._people[index])

        
#     def test_if_search_person_return_none(self):
#         '''Test if the search_person method fails and 
#         return none if it dosen't find the person in
#         the list'''

#         name = 'person_name'
#         other_name = "unknow_name"
        
#         my_list = Persons([name])
        
#         person_finded = my_list.search_person(other_name)
#         self.assertEqual(None, person_finded)

#     def test_if_remove_the_right_person_from_the_list_and_decrement_the_list(self):
#         '''tests if the remove_person remove 
#         the person from the list and decrements the list'''
#         name = 'person_name'
#         my_list = Persons([name])

#         self.assertEqual(True, my_list.remove_person(name))
#         self.assertEqual(len(my_list._people), 0)

#     def test_if_show_all_return_all_persons_from_the_list(self):
#         '''Tests if the show_all return all the Person Objects from the 
#         Persons Object
#         '''
#         name = 'person_name'
        
#         my_list = Persons([name])

#         self.assertEqual(my_list.show_all(), my_list._people)

