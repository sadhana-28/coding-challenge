CESS_RATE = 0.04


def calculate_tax(taxable_income):
    if taxable_income <= 700000:
        return 0, 0, 0

    tax = 0
    slabs = [
        (300000, 0),
        (600000, 0.05),
        (900000, 0.10),
        (1200000, 0.15),
        (1500000, 0.20)
    ]

    prev = 0
    for limit, rate in slabs:
        if taxable_income > limit:
            tax += (limit - prev) * rate
            prev = limit
        else:
            tax += (taxable_income - prev) * rate
            break
    else:
        tax += (taxable_income - 1500000) * 0.30

    cess = tax * CESS_RATE
    total_tax = tax + cess

    return tax, cess, total_tax


if __name__ == "__main__":
    tax, cess, total = calculate_tax(970000)

    print(f"Tax: ₹{tax:,.2f}")
    print(f"Cess (4%): ₹{cess:,.2f}")
    print(f"Total Tax Payable: ₹{total:,.2f}")
