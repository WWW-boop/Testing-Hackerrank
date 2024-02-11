from funny_string.funny_string_utils import funnyString
import unittest

class Funny_String(unittest.TestCase):
    def test_give_acxz_should_Funny(self):
        s = "acxz"
        expected_output = "Funny"
        
        result = funnyString(s)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')

    def test_give_bcxz_should_Not_Funny(self):
        s = "bcxz"
        expected_output = "Not Funny"
        
        result = funnyString(s)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')