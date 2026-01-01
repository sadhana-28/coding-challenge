import pytest
from challenges.tax_check import check_tax_eligibility


def test_salary_above_threshold():
    assert check_tax_eligibility("Ravi", 500000) == "Ravi must pay tax"


def test_salary_below_threshold():
    assert check_tax_eligibility("Anita", 250000) == "Anita does not need to pay tax"


def test_salary_equal_threshold():
    assert check_tax_eligibility("Suresh", 300000) == "Suresh does not need to pay tax"


def test_salary_decimal_value():
    assert check_tax_eligibility("Kiran", 300000.50) == "Kiran must pay tax"


def test_negative_salary():
    with pytest.raises(ValueError):
        check_tax_eligibility("Meena", -10000)


def test_invalid_salary_type():
    with pytest.raises(ValueError):
        check_tax_eligibility("Rahul", "300000")


def test_invalid_name():
    with pytest.raises(ValueError):
        check_tax_eligibility("", 400000)
