"""

"""


class Chapter:

    def title(self) -> str:
        """

        :return:
        """

        raise NotImplementedError()

    def content(self) -> str:
        """

        :return:
        """

        raise NotImplementedError()

    def count_char(self) -> int:
        """

        :return:
        """
        total = len(self.title()) + len(self.content())
        return total

    def count_words(self) -> int:
        """

        :return:
        """
        total = len(self.title().split(' ')) + len(self.content().split(' '))
        return total
