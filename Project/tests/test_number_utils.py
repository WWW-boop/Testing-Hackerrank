from coe_number.number_utils import is_prime_list
import unittest


class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
        
    def test_give_11_13_17_23_31_is_prime(self):
        prime_list = [11, 13, 17, 23, 31]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_11_31_29_2_101_7_is_prime(self):
        prime_list = [11, 31, 29, 2, 101, 7]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_2_4_15_20_100_10000_is_not_prime(self):
        prime_list = [2, 4, 15, 100, 10000]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_11_13_17_23_24_31_is_not_prime(self):
        prime_list = [11, 13, 17, 23, 24, 31]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_11_24_13_17_23_31_4_is_not_prime(self):
        prime_list = [11, 24, 13, 17, 23, 31, 4]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)