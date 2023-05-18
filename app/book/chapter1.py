
from app.core import Chapter


class Chapter1(Chapter):
    _title = "Chapter 1 title"
    _content = "This is the first chapter content.\nIt is multiline.\nBecause it is a chapter, not a title"

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
