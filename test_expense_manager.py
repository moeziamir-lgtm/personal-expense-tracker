import unittest
from expense_manager import is_valid_amount

class TestValidAmount(unittest.TestCase):

    def test_positive_amount(self):
        self.assertTrue(is_valid_amount(20))

    def test_zero_amounr(self):
        self.assertFalse(is_valid_amount(0))  

    def test_negative_amount(self):
        self.assertFalse(is_valid_amount(-20))      


if __name__ == "__main__":
    unittest.main()
