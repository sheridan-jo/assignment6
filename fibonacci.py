"""
Python Development II
Assignment 6 - A Fibonacci Series Iterable
John O.
December 4, 2024

This program contains an iterable which produces an iterator of the
Fibonacci series for a given value.

Usage:
A position is entered into the constructor for which
a Fibonacci series is generated.

Documented according to Google Style Docstrings
https://google.github.io/styleguide/pyguide.html
"""

class Fibonacci:
    """
    An iterable for creating a Fibonacci series

    Args:
        position (int): Position in the sequence up to which values are generated

    Attributes:
        current_count (int): Keeps track of number of Fibonacci numbers generated
        current_number (int): Tracks current Fibonacci number, initialized as 0
        next_number (int): Tracks next Fibonacci number, initialized as 1
    """

    def __init__(self, position):
        """
        Constructor requires a single positional argument
        which must be an integer.
        """

        self.position = position  # Position in the sequence up to which values are generated
        self.current_count = 0  #  Keeps track of number of Fibonacci numbers generated
        self.current_number = 0  #  Tracks current Fibonacci number, initialized as 0
        self.next_number = 1  #  Tracks next Fibonacci number, initialized as 1

        #  Raises ValueError for non-integer input
        if not isinstance(position, int):
            raise ValueError(f'{position} is not an integer.')

    def __iter__(self):
        """Returns the instance of Fibonacci class as an iterator"""
        return self

    def __next__(self):
        """Defines the instance of Fibonacci class as an iterator"""

        #  Stops iteration when the number of iterations is greater than position
        if self.current_count > self.position:
            raise StopIteration

        # Updates and returns the next Fibonacci number, starting from 0

        return_value = self.current_number  #  Value returned, starting from 0
        next_number = self.current_number + self.next_number  #  Adds previous 2 numbers
        self.current_number = self.next_number  #  Updates current number to next in the sequence
        self.next_number = next_number  # Updates the next number in the sequence

        self.current_count += 1  #  Counter incremented for next iteration
        return return_value  #  Returns the current Fibonacci number
