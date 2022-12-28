from funcs import factorial
import pytest


def test_factorial_0():
    assert factorial(0) == 1, "failed factorial(0)"


def test_factorial_1():
    assert factorial(1) == 1, "failed factorial(1)"


def test_factorial_5():
    assert factorial(5) == 120, "failed factorial(5)"


def test_factorial_8():
    assert factorial(8) == 40320, "failed factorial(8)"


def test_factorial_13():
    assert factorial(13) == 6227020800, "failed factorial(13)"
