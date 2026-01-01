import pytest
from challenges.swap_numbers import swap_numbers


def test_positive_numbers():
    assert swap_numbers(10, 20) == (20, 10)


def test_negative_numbers():
    assert swap_numbers(-5, -15) == (-15, -5)


def test_mixed_numbers():
    assert swap_numbers(-10, 25) == (25, -10)


def test_zero_values():
    assert swap_numbers(0, 5) == (5, 0)


def test_decimal_values():
    assert swap_numbers(2.5, 7.5) == (7.5, 2.5)


def test_same_values():
    assert swap_numbers(10, 10) == (10, 10)


def test_invalid_input():
    with pytest.raises(ValueError):
        swap_numbers("10", 5)
