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

    def count(self) -> int:
        """

        :return:
        """
        total = self.title().__len__() + self.content().__len__()
        return total
