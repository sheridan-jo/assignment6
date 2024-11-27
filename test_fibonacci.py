"""
Python Development II
Assignment 6 - A Fibonacci Series Iterable
Test Suite for fibonacci.py module
John O.
November 26, 2024

This is a test suite for the fibonacci.py module which tests its
properties and methods.

Usage:
Run this test module using pytest.

Imports:
    Fibonacci: Contains the Fibonacci class
    pytest: Used to test prime.py

Documented according to Google Style Docstrings
https://google.github.io/styleguide/pyguide.html

"""

import pytest
from fibonacci import Fibonacci

def test_non_integer():
    """Test that non-integer input raises ValueError"""
    with pytest.raises(ValueError):
        Fibonacci(3.14)
