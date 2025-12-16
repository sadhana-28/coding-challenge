def calculate_salary(name, emp_id, basic_salary, special_allowance, bonus_percent):
    gross_monthly_salary = basic_salary + special_allowance
    annual_bonus = (gross_monthly_salary * 12) * (bonus_percent / 100)
    annual_gross_salary = (gross_monthly_salary * 12) + annual_bonus

    return {
        "Name": name,
        "EmpID": emp_id,
        "Gross Monthly Salary": gross_monthly_salary,
        "Annual Gross Salary": annual_gross_salary
    }


if __name__ == "__main__":
    result = calculate_salary("John", "E12345", 70000, 15000, 10)

    for k, v in result.items():
        print(f"{k}: ₹{v:,.2f}" if isinstance(v, (int, float)) else f"{k}: {v}")
