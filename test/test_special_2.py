
"""
Special pages unit test
"""

import unittest
from book import SpecialPages


class MyTestCase(unittest.TestCase):
    """
    Special pages unit test class
    """

    @classmethod
    def setUpClass(cls):
        """
        Init class called one time before tests
        """

        cls.special = SpecialPages()  # Create the tested class instance

    def test_special_title(self):
        """
        Test the exact chapter title
        """
        title = self.special.title()
        # REM: assert(Expected, Actual)
        self.assertEqual("The book title", title)


if __name__ == '__main__':
    unittest.main()
