import pytest
from challenges.leap_year import is_leap_year


def test_regular_leap_year():
    assert is_leap_year(2024) is True


def test_century_non_leap_year():
    assert is_leap_year(1900) is False


def test_century_leap_year():
    assert is_leap_year(2000) is True


def test_non_leap_year():
    assert is_leap_year(2023) is False


def test_year_divisible_by_4_only():
    assert is_leap_year(2016) is True


def test_invalid_year_zero():
    with pytest.raises(ValueError):
        is_leap_year(0)


def test_negative_year():
    with pytest.raises(ValueError):
        is_leap_year(-2024)


def test_invalid_input_type():
    with pytest.raises(ValueError):
        is_leap_year("2024")
