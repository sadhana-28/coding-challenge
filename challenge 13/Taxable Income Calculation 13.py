STANDARD_DEDUCTION = 50000


def calculate_taxable_income(annual_gross_salary):
    taxable_income = max(0, annual_gross_salary - STANDARD_DEDUCTION)
    return annual_gross_salary, STANDARD_DEDUCTION, taxable_income


if __name__ == "__main__":
    gross, deduction, taxable = calculate_taxable_income(1020000)

    print(f"Annual Gross Salary: ₹{gross:,.2f}")
    print(f"Standard Deduction: ₹{deduction:,.2f}")
    print(f"Taxable Income: ₹{taxable:,.2f}")
