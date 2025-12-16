def calculate_item_total(item_code, description, quantity, price):
    """
    Calculates total cost for a single item.
    """

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    if price <= 0:
        raise ValueError("Price must be greater than zero")

    total_cost = quantity * price

    return {
        "Item Code": item_code,
        "Description": description,
        "Quantity": quantity,
        "Price per Unit": price,
        "Total Cost": total_cost
    }


if __name__ == "__main__":
    # Input from user
    item_code = input("Enter Item Code: ")
    description = input("Enter Item Description: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price per Unit: "))

    try:
        result = calculate_item_total(item_code, description, quantity, price)

        print("\nItem Details")
        print("-" * 25)
        for key, value in result.items():
            if isinstance(value, (int, float)):
                print(f"{key:15}: ₹{value:,.2f}")
            else:
                print(f"{key:15}: {value}")

    except ValueError as error:
        print("Error:", error)
