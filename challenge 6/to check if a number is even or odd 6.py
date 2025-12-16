def check_even_or_odd(number):
    """
    Determines whether a number is even or odd.

    Parameters:
    number (int): Input integer

    Returns:
    str: "Even" or "Odd"

    Raises:
    ValueError: If input is not an integer
    """

    # Input validation
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")

    if number % 2 == 0:
        return "Even"
    return "Odd"


if __name__ == "__main__":
    num = 7
    result = check_even_or_odd(num)
    print(f"{num} is {result}")
