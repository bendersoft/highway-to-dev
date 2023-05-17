
from app.core import Chapter


class Chapter2(Chapter):
    _title = "Chapter 2 title"
    _content = "Chapter 2 content"

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

    def count(self) -> int:
        """

        :return:
        """
        total = self.title().__len__() + self.content().__len__()
        return total