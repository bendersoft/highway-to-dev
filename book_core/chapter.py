
"""
Parent class for chapters
"""


class Chapter:
    """
    Chapter parent class
    Inherit this class to create a new chapter.
    """

    def title(self) -> str:
        """
        :return: the chapter title
        """

        raise NotImplementedError()

    def content(self) -> str:
        """
        :return: the chapter content
        """

        raise NotImplementedError()

    def count_char(self) -> int:
        """
        Count the number of character in the chapter.
        :return: char count
        """
        total = len(self.title()) + len(self.content())
        return total

    def count_words(self) -> int:
        """
        Count the number of words in the chapter.
        :return: word count
        """
        total = len(self.title().split(' ')) + len(self.content().split(' '))
        return total
