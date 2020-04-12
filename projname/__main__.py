"""
The application entry-point.

This file allows us to run the application using `python -m projname`.

For details see: https://docs.python.org/3/library/runpy.html
"""

import sys
import projname


def main(argv):
    """
    The application main function
    """
    print(f"Name: {__name__}")
    print(f"Package: {__package__}")
    print(f"Output: {projname.itworks()}")
    print(f"Args: {repr(argv)}")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
