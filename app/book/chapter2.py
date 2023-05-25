"""
Chapter 2
"""


from app.core import Chapter


class Chapter2(Chapter):
    """
    Chapter 2 definition class
    """

    _title = "Chapter 2 title"
    _content = "This is the second chapter content.\nIt is multiline, you know?.\nBecause it is a chapter."

    def title(self) -> str:
        """
        :return: the chapter title
        """

        return self._title

    def content(self) -> str:
        """
        :return: the chapter content
        """

        return self._content
