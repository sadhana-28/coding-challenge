def calculate_discount(total_amount, discount_rate):
    """
    Calculates the discount and final payable amount.

    Parameters:
    total_amount (int | float): Total bill amount
    discount_rate (int | float): Discount percentage (0–100)

    Returns:
    tuple: (discount_amount, final_amount)

    Raises:
    ValueError: For invalid or out-of-range inputs
    """

    # Input validation
    if not all(isinstance(value, (int, float)) for value in (total_amount, discount_rate)):
        raise ValueError("Total amount and discount rate must be numeric")

    if total_amount < 0:
        raise ValueError("Total amount cannot be negative")

    if discount_rate < 0 or discount_rate > 100:
        raise ValueError("Discount rate must be between 0 and 100")

    discount_amount = (total_amount * discount_rate) / 100
    final_amount = total_amount - discount_amount

    return discount_amount, final_amount


if __name__ == "__main__":
    amount = 2500
    discount = 10

    discount_value, payable_amount = calculate_discount(amount, discount)
    print(f"Discount Amount: {discount_value}")
    print(f"Final Amount to Pay: {payable_amount}")
