from alternating_characters.alternating_characters_utils import alternatingCharacters
import unittest

class AlternatingCharectersTest(unittest.TestCase):
    def test_give_ABABABAB_should_0(self):
        s = "ABABABAB"
        expected_output = 0
        
        result = alternatingCharacters(s)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
        
    def test_give_AAABBBAABB_should_4(self):
        s = "BBBBB"
        expected_output = 4
        
        result = alternatingCharacters(s)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_AAABBBAABB_should_6(self):
        s = "AAABBBAABB"
        expected_output = 6
        
        result = alternatingCharacters(s)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
        
    def test_give_ABBABBAA_should_3(self):
        s = "ABBABBAA"
        expected_output = 3
        
        result = alternatingCharacters(s)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
    
    def test_give_BAABAAABAAABBBAABAAAAABABAAAABABBAABBBABBAAAABABBABAAAAABBABAABBBBAAAABBAABABAAAABABABBBABAAABBBBBBB_should_51(self):
        s = "BAABAAABAAABBBAABAAAAABABAAAABABBAABBBABBAAAABABBABAAAAABBABAABBBBAAAABBAABABAAAABABABBBABAAABBBBBBB"
        expected_output = 51
        
        result = alternatingCharacters(s)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
    
    def test_give_AAAABBAAAA_should_7(self):
        s = "AAAABBAAAA"
        expected_output = 7
        
        result = alternatingCharacters(s)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
        
    def test_give_ABBAABBBBBABBABBABBABAAABBBAABAAABAABBBABABAAABAAAABAAAAABAAAAAAABABAABBAABABABBABABAABAABAABABBBBAA_should_45(self):
        s = "ABBAABBBBBABBABBABBABAAABBBAABAAABAABBBABABAAABAAAABAAAAABAAAAAAABABAABBAABABABBABABAABAABAABABBBBAA"
        expected_output = 45
        
        result = alternatingCharacters(s)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
        
    def test_give_BABBBBBBBBBBABBBBBBBBABBBBBAABBBABBBBAABBBBBBABBBBBBBBBABBBBBBBBBBBBBABBBBBBBAABBBBBBABBBBBBABBABBBB_should_73(self):
        s = "BABBBBBBBBBBABBBBBBBBABBBBBAABBBABBBBAABBBBBBABBBBBBBBBABBBBBBBBBBBBBABBBBBBBAABBBBBBABBBBBBABBABBBB"
        expected_output = 73
        
        result = alternatingCharacters(s)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}')