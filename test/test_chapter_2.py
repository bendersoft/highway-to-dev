
import unittest

from app.book import Chapter2


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.chapter = Chapter2()

    def test_chapter2_title(self):
        """
        Test the exact chapter title
        """
        title = self.chapter.title()
        # REM: assert(Expected, Actual)
        self.assertEqual("Chapter 2 title", title)

    def test_chapter2_content(self):
        """
        Test the exact chapter content
        :return:
        """
        expected = "This is the second chapter content.\nIt is multiline, you know?.\nBecause it is a chapter."
        content = self.chapter.content()
        # REM: assert(Expected, Actual)
        self.assertEqual(expected, content)

    def test_chapter2_count_char(self):
        """
        Test the exact chapter length
        :return:
        """
        expected = 103
        content = self.chapter.count_char()
        # REM: assert(Expected, Actual)
        self.assertEqual(expected, content)

    def test_chapter2_count_words(self):
        """
        Test the exact chapter length
        :return:
        """
        expected = 17
        content = self.chapter.count_words()
        # REM: assert(Expected, Actual)
        self.assertEqual(expected, content)


if __name__ == '__main__':
    unittest.main()
