from challenges.farmer_sales import calculate_overall_and_chemical_free_sales


def test_sales_values():
    overall, chemical_free = calculate_overall_and_chemical_free_sales()

    assert overall == 14972800
    assert chemical_free == 12092800


def test_chemical_free_less_than_overall():
    overall, chemical_free = calculate_overall_and_chemical_free_sales()
    assert chemical_free < overall
