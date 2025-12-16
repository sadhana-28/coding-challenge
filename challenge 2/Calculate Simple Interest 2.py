def calculate_simple_interest(principal, rate, time):
    """
    Calculates simple interest based on principal, rate, and time.

    Parameters:
    principal (int | float): Principal amount
    rate (int | float): Rate of interest per annum
    time (int | float): Time in years

    Returns:
    float: Calculated simple interest

    Raises:
    ValueError: If inputs are non-numeric or negative
    """

    # Input validation
    if not all(isinstance(value, (int, float)) for value in (principal, rate, time)):
        raise ValueError("Principal, rate, and time must be numeric values")

    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Principal, rate, and time cannot be negative")

    simple_interest = (principal * rate * time) / 100
    return simple_interest


if __name__ == "__main__":
    p = 1000
    r = 5
    t = 2

    si = calculate_simple_interest(p, r, t)
    print(f"Simple Interest: {si}")
