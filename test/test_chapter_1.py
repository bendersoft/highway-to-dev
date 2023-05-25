
"""
Chapter 1 unit test
"""

import unittest
from book import Chapter1


class MyTestCase(unittest.TestCase):
    """
    Chapter 1 unit test class
    """

    @classmethod
    def setUpClass(cls):
        """
        Init class called one time before tests
        """

        cls.chapter_1 = Chapter1()  # Create the tested class instance

    def test_chapter1_title(self):
        """
        Test the exact chapter title
        """
        title = self.chapter_1.title()
        # REM: assert(Expected, Actual)
        self.assertEqual("Chapter 1 title", title)

    def test_chapter1_content(self):
        """
        Test the exact chapter content
        :return:
        """
        expected = "This is the first chapter content.\nIt is multiline.\nBecause it is a chapter, not a title"
        content = self.chapter_1.content()
        # REM: assert(Expected, Actual)
        self.assertEqual(expected, content)

    def test_chapter1_count_char(self):
        """
        Test the exact chapter length
        :return:
        """
        expected = 103
        content = self.chapter_1.count_char()
        # REM: assert(Expected, Actual)
        self.assertEqual(expected, content)

    def test_chapter1_count_words(self):
        """
        Test the exact chapter length
        :return:
        """
        expected = 18
        content = self.chapter_1.count_words()
        # REM: assert(Expected, Actual)
        self.assertEqual(expected, content)


if __name__ == '__main__':
    unittest.main()
