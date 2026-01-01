import pytest
from challenges.challenge_1 import calculate_sum_and_average


def test_positive_numbers():
    total, avg = calculate_sum_and_average(10, 20)
    assert total == 30
    assert avg == 15


def test_negative_numbers():
    total, avg = calculate_sum_and_average(-10, -20)
    assert total == -30
    assert avg == -15


def test_mixed_numbers():
    total, avg = calculate_sum_and_average(-10, 20)
    assert total == 10
    assert avg == 5


def test_zero_values():
    total, avg = calculate_sum_and_average(0, 0)
    assert total == 0
    assert avg == 0


def test_invalid_input():
    with pytest.raises(ValueError):
        calculate_sum_and_average("a", 10)
