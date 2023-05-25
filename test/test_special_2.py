
import unittest

from app.book import SpecialPages


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.special = SpecialPages()

    def test_special_title(self):
        """
        Test the exact chapter title
        """
        title = self.special.title()
        # REM: assert(Expected, Actual)
        self.assertEqual("The book title", title)


if __name__ == '__main__':
    unittest.main()
