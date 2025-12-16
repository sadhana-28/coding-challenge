def is_leap_year(year):
    """
    Determines whether a given year is a leap year.

    Parameters:
    year (int): Year to be checked

    Returns:
    bool: True if leap year, False otherwise

    Raises:
    ValueError: If year is not a positive integer
    """

    # Input validation
    if not isinstance(year, int):
        raise ValueError("Year must be an integer")

    if year <= 0:
        raise ValueError("Year must be a positive integer")

    # Leap year logic
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True

    return False


if __name__ == "__main__":
    year = 2024
    result = is_leap_year(year)
    print(f"{year} is a leap year: {result}")
