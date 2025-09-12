import unittest
import pytest
from src.classes.person_list import PersonList

@pytest.mark.parametrize("invalid_types", [
    int,
    float,
    str,
    bool,
    tuple,
    dict,
    None
])

class TestPersonList(unittest.TestCase):
    '''Test class for PersonList class'''

    def test_non_list_type_in_contruction_function(self, invalid_types):
        with self.assertRaises(ValueError):
                PersonList(invalid_types)