from two_characters.two_characters_utils import alternate
import unittest

class TwoCharatersTest(unittest.TestCase):
    def test_give_beabeefeab_should_5(self):
        s = "beabeefeab"
        expected_output = 5
        
        result = alternate(s)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')