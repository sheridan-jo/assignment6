"""
Python Development II
Assignment 6 - A Fibonacci Series Iterable
Test Suite for fibonacci.py module
John O.
December 4, 2024

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

def test_position_2():
    """
        Tests that [0,1,1] is returned with constructor value of 2
        if cast as a list.
    """
    assert list(Fibonacci(2)) == [0,1,1]

def test_position_4():
    """
        Tests that [0,1,1,2,3] is returned with constructor value of 4
        if cast as a list.
    """
    assert list(Fibonacci(4)) == [0,1,1,2,3]

def test_position_10():
    """
        Tests that [0,1,1,2,3,5,8,13,21,34,55] is returned with constructor value of 10
        if cast as a list.
    """
    assert list(Fibonacci(10)) == [0,1,1,2,3,5,8,13,21,34,55]

def test_negative_value():
    """
        Tests that the iterator produces an empty list with a negative constructor value
    """
    assert not list(Fibonacci(-6))
