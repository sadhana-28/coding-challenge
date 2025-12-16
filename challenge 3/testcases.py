import pytest
from challenges.discount_calculator import calculate_discount


def test_valid_discount():
    discount, final = calculate_discount(2000, 10)
    assert discount == 200
    assert final == 1800


def test_zero_discount():
    discount, final = calculate_discount(1500, 0)
    assert discount == 0
    assert final == 1500


def test_full_discount():
    discount, final = calculate_discount(1000, 100)
    assert discount == 1000
    assert final == 0


def test_decimal_values():
    discount, final = calculate_discount(999.99, 12.5)
    assert discount == pytest.approx(124.99875)
    assert final == pytest.approx(874.99125)


def test_large_amount():
    discount, final = calculate_discount(1_000_000, 20)
    assert discount == 200_000
    assert final == 800_000


def test_negative_amount():
    with pytest.raises(ValueError):
        calculate_discount(-1000, 10)


def test_invalid_discount_rate():
    with pytest.raises(ValueError):
        calculate_discount(1000, 150)


def test_invalid_input_type():
    with pytest.raises(ValueError):
        calculate_discount("1000", 10)
