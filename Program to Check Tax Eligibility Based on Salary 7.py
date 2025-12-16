def check_tax_eligibility(name, salary):
    """
    Checks whether a person must pay tax based on salary.

    Parameters:
    name (str): Name of the person
    salary (int | float): Annual salary

    Returns:
    str: Tax eligibility message

    Raises:
    ValueError: If inputs are invalid
    """

    # Input validation
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Name must be a non-empty string")

    if not isinstance(salary, (int, float)):
        raise ValueError("Salary must be a numeric value")

    if salary < 0:
        raise ValueError("Salary cannot be negative")

    # Business logic
    if salary > 300000:
        return f"{name} must pay tax"
    else:
        return f"{name} does not need to pay tax"


if __name__ == "__main__":
    person_name = "Mahesh"
    annual_salary = 350000

    result = check_tax_eligibility(person_name, annual_salary)
    print(result)
