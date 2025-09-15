'''This module is for test in the utils_manager module from
utils in the src directory'''
import unittest
from unittest.mock import patch, mock_open

from src.utils.utils_manager import open_json_file


class TestUtilsManager(unittest.TestCase):
    '''This class testes the UtilManager's
    functions'''

    def test_load_json_file_success(self):
        '''tests if the open_json_file returns the actual list'''
        fake_data = '["person_one", "person_two", "person_three"]'

        with patch('builtins.open', mock_open(read_data=fake_data)):
            
            data = open_json_file('fake_path.json')

            self.assertEqual(data[0], 'person_one')
            self.assertEqual(data[1], 'person_two')
            self.assertEqual(data[2], 'person_three')



            
