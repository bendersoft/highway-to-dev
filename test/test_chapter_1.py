
import unittest

from app.book import Chapter1


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.chapter = Chapter1()

    def test_chapter1_title(self):
        """
        Test the exact chapter title
        """
        title = self.chapter.title()
        # REM: assert(Expected, Actual)
        self.assertEqual("Chapter 1 title", title)

    def test_chapter1_content(self):
        """
        Test the exact chapter content
        :return:
        """
        expected = "This is the first chapter content.\nIt is multiline.\nBecause it is a chapter, not a title"
        content = self.chapter.content()
        # REM: assert(Expected, Actual)
        self.assertEqual(expected, content)

    def test_chapter1_count_char(self):
        """
        Test the exact chapter length
        :return:
        """
        expected = 103
        content = self.chapter.count_char()
        # REM: assert(Expected, Actual)
        self.assertEqual(expected, content)

    def test_chapter1_count_words(self):
        """
        Test the exact chapter length
        :return:
        """
        expected = 18
        content = self.chapter.count_words()
        # REM: assert(Expected, Actual)
        self.assertEqual(expected, content)


if __name__ == '__main__':
    unittest.main()
