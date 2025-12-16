def calculate_item_total(code, price, quantity):
    total = price * quantity

    if code == "PROMO10":
        total *= 0.90

    return total


if __name__ == "__main__":
    item_total = calculate_item_total("PROMO10", 500, 4)
    print(f"Item Total after Promo Discount: ₹{item_total:,.2f}")
