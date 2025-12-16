def swap_numbers(first, second):
    """
    Swaps two numeric values.

    Parameters:
    first (int | float): First number
    second (int | float): Second number

    Returns:
    tuple: (second, first)

    Raises:
    ValueError: If inputs are not numeric
    """

    # Input validation
    if not isinstance(first, (int, float)) or not isinstance(second, (int, float)):
        raise ValueError("Both inputs must be numeric values")

    # Pythonic swap using tuple unpacking
    first, second = second, first
    return first, second


if __name__ == "__main__":
    a = 5
    b = 10

    swapped_a, swapped_b = swap_numbers(a, b)
    print(f"After swapping: a = {swapped_a}, b = {swapped_b}")
