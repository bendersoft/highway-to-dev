
""" Main application entry point.

    python -m app

"""
from textwrap import dedent

from book import SpecialPages
from book import Chapter1
from book import Chapter2


def main() -> str:
    """ Execute the application.

    """
    special_pages = SpecialPages()
    chapter_1 = Chapter1()
    chapter_2 = Chapter2()

    content = f"""\
       {special_pages.title()}
       -----------------------
       =======================
       {chapter_1.title()}
       =======================
       {chapter_1.content()}
       =======================
       {chapter_2.title()}
       =======================
       {chapter_2.content()}
       .......................
       {special_pages.final()}
    """
    return content


# Make the script executable.
if __name__ == "__main__":

    BOOK = dedent(main())

    print(BOOK)
