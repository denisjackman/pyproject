import unittest

def is_prime(number):
    if number in (0, 1):
        return False
    for element in range(number):
        print(number)
        if number % element == 0:
            return False
    return True

class PrimesTestCase(unittest.TestCase):
    def test_is_five_prime(self):
        self.assertTrue(is_prime(5))
    def test_is_zero_not_prime(self):
        self.assertFalse(is_prime(0))



if __name__ == '__main__':
    unittest.main()
    print(is_prime(0))
    print(is_prime(5))
