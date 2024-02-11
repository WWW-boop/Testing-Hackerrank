from grid_challenge.grid_challenge_utils import gridChallenge
import unittest

class FunnyStringTest(unittest.TestCase):
    def test_give_ebacd_fghij_olmkn_trpqs_xywuv_should_YES(self):
        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        expected_output = "YES"
        
        result = gridChallenge(grid)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
    
    def test_give_abc_lmp_qrt_should_YES(self):
        grid = ['abc', 'lmp', 'qrt']
        expected_output = "YES"
        
        result = gridChallenge(grid)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')

    def test_give_mpxz_abcd_wlmf_should_NO(self):
        grid = ['mpxz', 'abcd', 'wlmf']
        expected_output = "NO"
        
        result = gridChallenge(grid)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')
    
    def test_give_abc_hjk_mpq_rtv_should_YES(self):
        grid = ['abc', 'hjk', 'mpq','rtv']
        expected_output = "YES"
        
        result = gridChallenge(grid)
        
        self.assertEqual(result,expected_output, f'Should be {expected_output}')