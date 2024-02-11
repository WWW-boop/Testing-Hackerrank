from caesar_cipher.caesar_cipher_utils import caesarCipher
import unittest

class Caesar_Cipher(unittest.TestCase):
    def test_give_middle_Outz_and_2_should_okffng_Qwvb(self):
        s = "middle-Outz"
        k = 2
        expected_output = "okffng-Qwvb"
        
        result = caesarCipher(s, k)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
    
    def test_give_D3q4_and_0_should_D3q4(self):
        s = "D3q4"
        k = 0
        expected_output = "D3q4"
        
        result = caesarCipher(s, k)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
        
    def test_give_Ciphering_and_26_Ciphering(self):
        s = "Ciphering."
        k = 26
        expected_output = "Ciphering."
        
        result = caesarCipher(s, k)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}') 
    
    def test_give_Pz_and_66_should_Dn(self):
        s = "Pz-/aI/J`EvfthGH"
        k = 66
        expected_output = "Dn-/oW/X`SjthvUV"
        
        result = caesarCipher(s, k)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
        
    def test_give_1X7T4Vr_and_27_1Y7U4Ws(self):
        s = "1X7T4VrCs23k4vv08D6yQ3S19G4rVP188M9ahuxB6j1tMGZs1m10ey7eUj62WV2exLT4C83zl7Q80M"
        k = 27
        expected_output = "1Y7U4WsDt23l4ww08E6zR3T19H4sWQ188N9bivyC6k1uNHAt1n10fz7fVk62XW2fyMU4D83am7R80N"
        
        result = caesarCipher(s, k)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
    
    def test_give_159357lcfd_and_98_should_159357fwzx(self):
        s = "159357lcfd"
        k = 98
        expected_output = "159357fwzx"
        
        result = caesarCipher(s, k)
        
        self.assertEqual(result, expected_output, f'Should be {expected_output}')  
    
    