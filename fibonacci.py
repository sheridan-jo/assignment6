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

    def __init__(self, max_count):
        """
        Constructor requires a single positional argument
        which must be an integer.
        """

        self.max_count = max_count  #  Maximum number of iterations

        self.current_count = 0  #  Keeps track of number of Fibonacci numbers generated

        #  Raises ValueError for non-integer input
        if not isinstance(max_count, int):
            raise ValueError(f'{max_count} is not an integer.')

    def __iter__(self):
        """Returns the instance of Fibonacci class as an iterator"""
        return self

    def __next__(self):
        """Defines the instance of Fibonacci class as an iterator"""

        # Handle the case where max_count is 0 by returning 0 once
        if self.max_count == 0 and self.current_count == 0:
            self.current_count += 1
            return 0

        #  Stop iteration when the number of iterations equals max_count
        if self.current_count >= self.max_count:
            raise StopIteration

        #  Counter incremented for next iteration
        self.current_count += 1

        # Return the current Fibonacci number
        return 0
