def find_largest_of_three(num1, num2, num3):
    """
    Finds the largest number among three numeric values.

    Parameters:
    num1 (int | float): First number
    num2 (int | float): Second number
    num3 (int | float): Third number

    Returns:
    int | float: The largest number

    Raises:
    ValueError: If any input is non-numeric
    """

    # Input validation
    if not all(isinstance(value, (int, float)) for value in (num1, num2, num3)):
        raise ValueError("All inputs must be numeric values")

    largest = num1

    if num2 > largest:
        largest = num2

    if num3 > largest:
        largest = num3

    return largest


if __name__ == "__main__":
    a = 15
    b = 25
    c = 10

    result = find_largest_of_three(a, b, c)
    print(f"The largest number is: {result}")
