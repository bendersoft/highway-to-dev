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
        total = self.title().__len__() + self.content().__len__()
        return total

    def count_words(self) -> int:
        """

        :return:
        """
        total = self.title().split(' ').__len__() + self.content().split(' ').__len__()
        return total
