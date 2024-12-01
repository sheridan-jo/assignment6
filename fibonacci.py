"""
Python Development II
Assignment 6 - A Fibonacci Series Iterable
John O.
December 1, 2024

This program contains an iterable which produces an iterator of the
Fibonacci series for a given value.

Usage:
A position is entered into the constructor for which
a Fibonacci series is generated.


Documented according to Google Style Docstrings
https://google.github.io/styleguide/pyguide.html
"""

class Fibonacci:
    """An iterable for creating a Fibonacci series"""

    def __init__(self, position):
        """
        Constructor requires a single positional argument
        which must be an integer.
        """

        self.position = position

        #  Raises ValueError for non-integer input
        if not isinstance(position, int):
            raise ValueError(f'{position} is not an integer.')

    def __iter__(self):
        """Returns the instance of Fibonacci class as an iterator"""
        return self

    def __next__(self):
        """Defines the instance of Fibonacci class as an iterator"""

        if self.position < 0:  #  Stop iteration for negative values
            raise StopIteration

        if self.position == 0:  #  Handling for position as 0

            #  Decrements position to ensure next call raises StopIteration
            self.position -= 1
            return 0
