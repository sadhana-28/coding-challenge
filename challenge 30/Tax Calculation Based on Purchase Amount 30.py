def calculate_tax(total):
    if total < 5000:
        tax = total * 0.05
    elif total <= 20000:
        tax = total * 0.10
    else:
        tax = total * 0.15

    final_total = total + tax

    print(f"Tax: ₹{tax:,.2f}")
    print(f"Total after Tax: ₹{final_total:,.2f}")


if __name__ == "__main__":
    calculate_tax(18000)
