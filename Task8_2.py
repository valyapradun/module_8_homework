"""
Write end-to-end test for task 7.6.
"""

import unittest
from Task7_6 import goldbach, is_prime
from Task7_5 import ValueTooSmallException, ValueTooLargeException, ValueIsOddException, ValueIsNotIntException


class TestEndToEnd(unittest.TestCase):

    def setUp(self) -> None:
        print(f'Starting test {self._testMethodName}...')

    def tearDown(self) -> None:
        print(f'Ending test {self._testMethodName}...')

    def test_goldbachRightValue(self):
        """Checking the correctness of the method goldbach"""
        self.assertEqual(goldbach(4), [3, 1])
        self.assertNotEqual(goldbach(8), [4, 4])
        self.assertEqual(goldbach(10), [3, 7])

    def test_is_prime(self):
        """Checking the correctness of the method is_prime"""
        self.assertTrue(is_prime(1))
        self.assertFalse(is_prime(8))
        self.assertEqual(is_prime(53), True)

    def test_goldbachTooSmallValue(self):
        """Checking for ValueTooSmallException exception if the argument is less than 3"""
        with self.assertRaises(ValueTooSmallException):
            goldbach(-10)
        with self.assertRaises(ValueTooSmallException):
            goldbach(3)

    def test_goldbachTooLargeValue(self):
        """Checking for ValueTooLargeException exception if the argument is greater than 100"""
        with self.assertRaises(ValueTooLargeException):
            goldbach(101)

    def test_goldbachIsOddValue(self):
        """Checking for ValueIsOddException exception if the argument is odd number"""
        with self.assertRaises(ValueIsOddException):
            goldbach(57)

    def test_goldbachIsNotIntValue(self):
        """Checking for ValueIsNotIntException exception if the argument is not integer"""
        with self.assertRaises(ValueIsNotIntException):
            goldbach("qwerty")


if __name__ == '__main__':
    unittest.main()



