import pytest
from challenges.even_odd import check_even_or_odd


def test_even_number():
    assert check_even_or_odd(10) == "Even"


def test_odd_number():
    assert check_even_or_odd(7) == "Odd"


def test_zero():
    assert check_even_or_odd(0) == "Even"


def test_negative_even():
    assert check_even_or_odd(-4) == "Even"


def test_negative_odd():
    assert check_even_or_odd(-9) == "Odd"


def test_invalid_input_float():
    with pytest.raises(ValueError):
        check_even_or_odd(3.5)


def test_invalid_input_string():
    with pytest.raises(ValueError):
        check_even_or_odd("10")
