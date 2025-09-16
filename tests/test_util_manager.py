'''This module is for test in the utils_manager module from
utils in the src directory'''
import unittest
import json
import pytest
from unittest.mock import patch, mock_open

from src.utils.utils_manager import open_json_file


class TestUtilsManager(unittest.TestCase):
    '''This class testes the UtilManager's
    functions'''

    def test_load_json_file_success(self):
        '''tests if the open_json_file returns the actual list'''
        fake_data = '["person_one", "person_two", "person_three"]'

        with patch('builtins.open', mock_open(read_data=fake_data)) as mock_file:
            
            data = open_json_file('fake_path.json')

            self.assertEqual(data[0], 'person_one')
            self.assertEqual(data[1], 'person_two')
            self.assertEqual(data[2], 'person_three')

        mock_file.assert_called_once_with('fake_path.json')

    def test_FileNotFoundError(self):
        '''This test guarantee that open_json_file 
        fails with the file was not find'''
        with patch('builtins.open') as mock_file:
            mock_file.side_effect = FileNotFoundError

            with pytest.raises(FileNotFoundError):
                open_json_file("fake_path.json")

    def test_JSONDecodeError(self):
        '''Tests a json file that is not possible 
        to decode.'''

        undecoded_json = '["person_one", "person_two" "person_three"]'

        with patch('builtins.open', mock_open(read_data=undecoded_json)):
            with pytest.raises(json.JSONDecodeError):
                open_json_file('fake_path.json')
            
