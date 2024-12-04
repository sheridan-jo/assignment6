"""
Python Development II
Assignment 6 - A Fibonacci Series Iterable
Test Suite for fibonacci.py module
John O.
December 3, 2024

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

def test_position_0():
    """
    Tests that [0] is returned with constructor value of 0
    if cast as a list.
    """
    assert list(Fibonacci(0)) == [0]

def test_position_1():
    """
    Tests that [0,1] is returned with constructor value of 1
    if cast as a list.
    """
    assert list(Fibonacci(1)) == [0,1]
