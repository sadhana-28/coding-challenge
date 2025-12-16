STANDARD_DEDUCTION = 50000
REBATE_LIMIT = 700000


def calculate_annual_salary(monthly_components):
    """
    Calculates annual gross salary from monthly components.
    """
    if not isinstance(monthly_components, dict):
        raise ValueError("Salary components must be provided as a dictionary")

    for value in monthly_components.values():
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Salary values must be non-negative numbers")

    monthly_total = sum(monthly_components.values())
    return monthly_total * 12


def calculate_taxable_income(gross_salary):
    """
    Applies standard deduction to compute taxable income.
    """
    return max(0, gross_salary - STANDARD_DEDUCTION)


def calculate_tax_new_regime(taxable_income):
    """
    Calculates tax as per New Tax Regime (2023).
    """

    if taxable_income <= REBATE_LIMIT:
        return 0

    tax = 0
    slabs = [
        (300000, 0.00),
        (600000, 0.05),
        (900000, 0.10),
        (1200000, 0.15),
        (1500000, 0.20),
    ]

    previous_limit = 0

    for limit, rate in slabs:
        if taxable_income > limit:
            tax += (limit - previous_limit) * rate
            previous_limit = limit
        else:
            tax += (taxable_income - previous_limit) * rate
            return tax

    tax += (taxable_income - 1500000) * 0.30
    return tax


def generate_tax_report(employee_name, monthly_salary_components):
    """
    Generates a complete tax report for an employee.
    """

    if not isinstance(employee_name, str) or not employee_name.strip():
        raise ValueError("Employee name must be a valid string")

    gross_salary = calculate_annual_salary(monthly_salary_components)
    taxable_income = calculate_taxable_income(gross_salary)
    tax_payable = calculate_tax_new_regime(taxable_income)
    net_salary = gross_salary - tax_payable

    return {
        "employee": employee_name,
        "gross_salary": gross_salary,
        "taxable_income": taxable_income,
        "tax_payable": tax_payable,
        "net_salary": net_salary
    }


if __name__ == "__main__":
    employee = "Ravi Kumar"
    salary = {
        "Basic": 50000,
        "HRA": 20000,
        "Allowances": 10000
    }

    report = generate_tax_report(employee, salary)

    print("Employee Tax Report")
    print("-------------------")
    print("Employee Tax Report")
print("-------------------")

for key, value in report.items():
    label = key.replace("_", " ").title()

    if isinstance(value, (int, float)):
        print(f"{label:20}: ₹{value:,.2f}")
    else:
        print(f"{label:20}: {value}")
