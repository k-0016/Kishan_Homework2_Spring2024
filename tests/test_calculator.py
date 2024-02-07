# tests/test_calculator.py

"""
This module contains tests for the calculator module functions.
"""

import pytest  # Standard library imports first
from calculator import add, subtract, multiply, divide  # Local application imports next

def test_add():
    """Test adding two numbers."""
    assert add(2, 3) == 5

def test_subtract():
    """Test subtracting two numbers."""
    assert subtract(5, 3) == 2

def test_multiply():
    """Test multiplying two numbers."""
    assert multiply(2, 3) == 6

def test_divide():
    """Test dividing two numbers."""
    assert divide(6, 3) == 2

def test_divide_by_zero():
    """Test dividing by zero raises ValueError."""
    with pytest.raises(ValueError):
        divide(1, 0)
