
from app.core import Chapter


class Chapter2(Chapter):
    _title = "Chapter 2 title"
    _content = "This is the second chapter content.\nIt is multiline, you know?.\nBecause it is a chapter."

    def title(self) -> str:
        """

        :return:
        """

        return self._title

    def content(self) -> str:
        """

        :return:
        """

        return self._content
