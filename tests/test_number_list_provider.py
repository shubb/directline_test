import unittest
from services.number_list_provider import get_list_of_numbers

class TestNumberListProvider(unittest.TestCase):
    def test_number_list_provider(self):
        
        list_of_numbers_result = get_list_of_numbers()
        list_of_numbers_expected_result = list(range(10000001))

        # Check the list of numbers function returns the expected list
        self.assertListEqual(list_of_numbers_result, list_of_numbers_expected_result)
    
