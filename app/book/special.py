
from app.core import Special


class SpecialPages(Special):

    _title = "The book title"
    _final = "The book final"
    _cover = "The book cover"
    _resume = "The book resume"

    def title(self) -> str:
        """

        :return:
        """

        return self._title

    def final(self) -> str:
        """

        :return:
        """

        return self._final

    def cover(self) -> str:
        """

        :return:
        """

        return self._cover

    def resume(self) -> str:
        """

        :return:
        """

        return self._resume
