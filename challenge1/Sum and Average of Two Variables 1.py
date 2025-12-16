def calculate_sum_and_average(a, b):
    """
    Calculates the sum and average of two numbers.

    Parameters:
    a (int or float): First number
    b (int or float): Second number

    Returns:
    tuple: (sum, average)
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Inputs must be numeric")

    total = a + b
    average = total / 2
    return total, average


# Sample execution
if __name__ == "__main__":
    x = 10
    y = 20
    total, avg = calculate_sum_and_average(x, y)
    print(f"Sum: {total}")
    print(f"Average: {avg}")
