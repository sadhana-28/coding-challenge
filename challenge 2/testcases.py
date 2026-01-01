import pytest
from challenges.simple_interest import calculate_simple_interest


def test_positive_values():
    assert calculate_simple_interest(1000, 5, 2) == 100.0


def test_zero_values():
    assert calculate_simple_interest(0, 5, 2) == 0
    assert calculate_simple_interest(1000, 0, 2) == 0
    assert calculate_simple_interest(1000, 5, 0) == 0


def test_decimal_values():
    assert calculate_simple_interest(1500.5, 4.5, 1.5) == pytest.approx(101.28375)


def test_large_values():
    assert calculate_simple_interest(1_000_000, 10, 5) == 500_000


def test_negative_values():
    with pytest.raises(ValueError):
        calculate_simple_interest(-1000, 5, 2)


def test_invalid_input_types():
    with pytest.raises(ValueError):
        calculate_simple_interest("1000", 5, 2)
