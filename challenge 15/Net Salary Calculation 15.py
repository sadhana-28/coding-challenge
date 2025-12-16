def calculate_net_salary(annual_gross_salary, total_tax):
    net_salary = annual_gross_salary - total_tax
    return net_salary


if __name__ == "__main__":
    net = calculate_net_salary(1020000, 76800)

    print(f"Annual Net Salary: ₹{net:,.2f}")
