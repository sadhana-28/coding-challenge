def calculate_grand_total():
    grand_total = 0

    while True:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter quantity: "))

        item_total = price * quantity
        grand_total += item_total

        choice = input("Add another item? (y/n): ").lower()
        if choice != 'y':
            break

    print(f"\nGrand Total: ₹{grand_total:,.2f}")


if __name__ == "__main__":
    calculate_grand_total()
