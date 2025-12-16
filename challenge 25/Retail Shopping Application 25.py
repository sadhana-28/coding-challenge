def generate_invoice(items):
    subtotal = sum(item["price"] * item["quantity"] for item in items)

    surcharge = 0
    for item in items:
        if item["quantity"] > 10:
            surcharge = subtotal * 0.02
            break

    discount = 0
    if subtotal >= 10000:
        discount = subtotal * 0.10
    elif subtotal >= 5000:
        discount = subtotal * 0.05

    taxable_amount = subtotal - discount + surcharge
    gst = taxable_amount * 0.05
    total_payable = taxable_amount + gst

    return {
        "subtotal": subtotal,
        "discount": discount,
        "surcharge": surcharge,
        "gst": gst,
        "total": total_payable
    }


def print_invoice(items, bill):
    print("\n🧾 RETAIL SHOPPING INVOICE")
    print("-" * 35)

    for item in items:
        print(f"{item['name']:15} {item['quantity']:3} × ₹{item['price']:,.2f}")

    print("-" * 35)
    print(f"Subtotal       : ₹{bill['subtotal']:,.2f}")
    print(f"Discount       : ₹{bill['discount']:,.2f}")
    print(f"Surcharge      : ₹{bill['surcharge']:,.2f}")
    print(f"GST (5%)       : ₹{bill['gst']:,.2f}")
    print("-" * 35)
    print(f"TOTAL PAYABLE  : ₹{bill['total']:,.2f}")


if __name__ == "__main__":
    items = [
        {"name": "Shirt", "price": 1200, "quantity": 2},
        {"name": "Jeans", "price": 2500, "quantity": 1},
        {"name": "Socks", "price": 150, "quantity": 12}
    ]

    bill = generate_invoice(items)
    print_invoice(items, bill)
