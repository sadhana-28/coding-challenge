def generate_report(details):
    print("\nEmployee Tax Report")
    print("-" * 30)

    for key, value in details.items():
        if isinstance(value, (int, float)):
            print(f"{key:25}: ₹{value:,.2f}")
        else:
            print(f"{key:25}: {value}")


if __name__ == "__main__":
    report_data = {
        "Name": "John Doe",
        "EmpID": "E12345",
        "Gross Monthly Salary": 85000,
        "Annual Gross Salary": 1020000,
        "Taxable Income": 970000,
        "Tax Payable": 76800,
        "Annual Net Salary": 943200
    }

    generate_report(report_data)
