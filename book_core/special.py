
"""
Parent class for a book special section
"""


class Special:
    """
    Special pages parent class
    Inherit this class to create a new book.
    """
    def title(self) -> str:
        """
        :return: the book title
        """

        raise NotImplementedError()

    def final(self) -> str:
        """
        :return: the book final page
        """

        raise NotImplementedError()

    def cover(self) -> str:
        """
        :return: the book cover
        """

        raise NotImplementedError()

    def resume(self) -> str:
        """
        :return: the book resume
        """

        raise NotImplementedError()
