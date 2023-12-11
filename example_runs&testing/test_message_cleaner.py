"""
This is a test file to test functions in message_cleaner.py\
"""

import unittest
from message_cleaner import get_time, generate_id, get_username, get_keyword


class TestFunctions(unittest.TestCase):

    def test_get_time(self):
        """
        test the function get_time in message_cleaner.py
        """
        # Test with default time format
        self.assertEqual(get_time(1701988859), '2023-12-07 22:40')

        # Test with custom time format
        self.assertEqual(get_time(1701988859, "%Y-%m-%d"), '2023-12-07')

        # Test with 0 value
        self.assertEqual(get_time(0), '')

        # Test with None value
        self.assertEqual(get_time(None), '')

    def test_generate_id(self):
        """
        test the function generate_id in message_cleaner.py
        group chat id is negative int,
        private group id is positive int.
        """
        # Test with positive integer
        self.assertEqual(generate_id(1002005006416, 69), '1002005006416_69')

        # Test with positive integer
        self.assertEqual(generate_id(1002005006416, 69), '1002005006416_69')

        # Test with None value
        self.assertEqual(generate_id(None, None), 'None_None')

    def test_get_username(self):
        """
        test the function get_username in message_cleaner.py
        """
        # Test get_username function with different cases
        self.assertEqual(get_username('Jerry', None), 'Jerry')
        self.assertEqual(get_username(None, None), '')
        self.assertEqual(get_username('Alice', 'Potter'), 'Alice Potter')

    def test_get_keyword(self):
        """
        test the function get_keyword in message_cleaner.py
        """
        # Test with symbol == '$'
        self.assertEqual(get_keyword("check out $tsla Elon will launch a rocket.", "$"), 'tsla')

        # Test with symbol == '#'
        self.assertEqual(get_keyword("check out #tsla Elon will launch a rocket.", "#"), 'tsla')

        # Test get_keyword with multiple symbols in the message
        self.assertEqual(get_keyword("check out $tsla and #aapl Elon will launch a rocket.", "$"), 'tsla')

        # Test get_keyword with symbols at the end of the message
        self.assertEqual(get_keyword("Check out the latest news! #stocks", "#"), 'stocks')

        # Test get_keyword with symbols in the middle of the message
        self.assertEqual(get_keyword("Exciting news $AAPL today! #stocks", "$"), 'aapl')

        # Test get_keyword with no symbol in the message
        self.assertEqual(get_keyword("No symbol in this message", "$"), '')


if __name__ == '__main__':
    unittest.main()
