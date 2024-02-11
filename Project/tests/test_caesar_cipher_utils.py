from caesar_cipher.caesar_cipher_utils import caesarCipher
import unittest

class Caesar_Cipher(unittest.TestCase):
    def test_give_middle_Outz_and_2_should_okffng_Qwvb(self):
        s = "middle-Outz"
        k = 2
        expected_output = "okffng-Qwvb"
        
        result = caesarCipher(s, k)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}')