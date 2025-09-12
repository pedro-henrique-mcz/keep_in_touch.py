import unittest
from src.classes.person import Person

class TestPerson(unittest.TestCase):

    def test_name_validation_wit_empty_name(self):
        with self.assertRaises(ValueError):
            Person("")

    def test_name_validation_with_non_string_names(self):
        invalid_types = [1, 1.1, 2j, [1], (1,2), {"one":1}, True]
        
        for invalid_type in invalid_types:
            with self.assertRaises(ValueError):
                Person(invalid_type)



