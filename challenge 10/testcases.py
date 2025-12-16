import pytest
from challenges.student_report_card import generate_report_card


def test_first_class():
    result = generate_report_card("Ravi", [70, 65, 60])
    assert result["class"] == "First Class"


def test_second_class():
    result = generate_report_card("Anita", [55, 50, 52])
    assert result["class"] == "Second Class"


def test_pass_class():
    result = generate_report_card("Suresh", [40, 35, 38])
    assert result["class"] == "Pass Class"


def test_fail_class():
    result = generate_report_card("Meena", [30, 25, 20])
    assert result["class"] == "Fail"


def test_boundary_values():
    assert generate_report_card("A", [60, 60, 60])["class"] == "First Class"
    assert generate_report_card("B", [50, 50, 50])["class"] == "Second Class"
    assert generate_report_card("C", [35, 35, 35])["class"] == "Pass Class"


def test_invalid_marks_count():
    with pytest.raises(ValueError):
        generate_report_card("Kiran", [80, 90])


def test_invalid_mark_value():
    with pytest.raises(ValueError):
        generate_report_card("Kiran", [80, -10, 90])


def test_invalid_name():
    with pytest.raises(ValueError):
        generate_report_card("", [60, 60, 60])
