import pytest
from challenges.largest_of_three import find_largest_of_three


def test_distinct_numbers():
    assert find_largest_of_three(10, 20, 30) == 30


def test_first_is_largest():
    assert find_largest_of_three(50, 20, 30) == 50


def test_second_is_largest():
    assert find_largest_of_three(10, 40, 30) == 40


def test_third_is_largest():
    assert find_largest_of_three(10, 20, 60) == 60


def test_all_equal():
    assert find_largest_of_three(25, 25, 25) == 25


def test_two_equal_largest():
    assert find_largest_of_three(30, 30, 10) == 30


def test_negative_numbers():
    assert find_largest_of_three(-10, -5, -20) == -5


def test_decimal_values():
    assert find_largest_of_three(2.5, 3.7, 3.6) == 3.7


def test_invalid_input():
    with pytest.raises(ValueError):
        find_largest_of_three(10, "20", 30)
