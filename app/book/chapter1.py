
from app.core import Chapter


class Chapter1(Chapter):
    _title = "Chapter 1 title"
    _content = "Chapter 1 content"

    def title(self) -> str:
        """

        :return:
        """

        return self._title

    def content(self) -> str:
        """

        :return:
        """
        content = "Chapter 1 title"

        return self._content

    def count(self) -> int:
        """

        :return:
        """
        total = self.title().__len__() + self.content().__len__()
        return total
