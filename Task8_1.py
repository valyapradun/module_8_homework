"""
Using mock write unit test for task 7.6.
"""

from unittest.mock import patch
import Task7_6
import unittest


@patch('builtins.input')
@patch('builtins.print')
class TestMock(unittest.TestCase):

    def setUp(self) -> None:
        print(f'Starting test {self._testMethodName}...')

    def tearDown(self) -> None:
        print(f'Ending test {self._testMethodName}...')

    def test_inputExitValue(self, print_mock, input_mock):
        """Checking the correctness input for exit ('q')"""
        input_mock.return_value = 'q'
        Task7_6.main()
        input_mock.assert_called_once_with('Enter a number (press "q" to exit): ')
        print_mock.assert_not_called()

    def test_inputRightValue(self, print_mock, input_mock):
        """Checking the correctness input ('8')"""
        input_mock.side_effect = ['8', 'q']
        Task7_6.main()
        self.assertEqual(input_mock.call_count, 2)
        print_mock.assert_called_once_with('Result: [3, 5]')

    def test_inputTooSmallValue(self, print_mock, input_mock):
        """Checking the incorrectness input (too small value)"""
        input_mock.side_effect = ['1', 'q']
        Task7_6.main()
        self.assertEqual(input_mock.call_count, 2)
        print_mock.assert_called_once_with('Number 1 must be greater than 3\nTry again!\n')

    def test_inputTooLargeValue(self, print_mock, input_mock):
        """Checking the incorrectness input (too large value)"""
        input_mock.side_effect = ['124', 'q']
        Task7_6.main()
        self.assertEqual(input_mock.call_count, 2)
        print_mock.assert_called_once_with('Number 124 must be less than 100\nTry again!\n')

    def test_inputOddValue(self, print_mock, input_mock):
        """Checking the incorrectness input (odd value)"""
        input_mock.side_effect = ['57', 'q']
        Task7_6.main()
        self.assertEqual(input_mock.call_count, 2)
        print_mock.assert_called_once_with('Number 57 must be even\nTry again!\n')

    def test_inputNotIntValue(self, print_mock, input_mock):
        """Checking the incorrectness input (not int value)"""
        input_mock.side_effect = ['qwerty', 'q']
        Task7_6.main()
        self.assertEqual(input_mock.call_count, 2)
        print_mock.assert_called_once_with('Number qwerty should be integer\nTry again!\n')


if __name__ == '__main__':
    unittest.main()
