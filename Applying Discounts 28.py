def apply_discounts(grand_total, total_quantity):
    if grand_total > 10000:
        grand_total *= 0.90  # 10% discount

    if total_quantity > 20:
        grand_total *= 0.95  # additional 5% discount

    print(f"Discounted Total: ₹{grand_total:,.2f}")


if __name__ == "__main__":
    apply_discounts(12000, 25)
