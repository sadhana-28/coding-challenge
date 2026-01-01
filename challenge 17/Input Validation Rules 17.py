def validate_inputs(name, emp_id, basic, allowance, bonus):
    if not name.isalpha():
        raise ValueError("Name must contain only alphabets")

    if not emp_id.isalnum() or not (5 <= len(emp_id) <= 10):
        raise ValueError("EmpID must be alphanumeric (5–10 characters)")

    if basic <= 0 or allowance < 0:
        raise ValueError("Invalid salary values")

    if not (0 <= bonus <= 100):
        raise ValueError("Bonus must be between 0 and 100")

    return True


if __name__ == "__main__":
    try:
        validate_inputs("John", "E12345", 70000, 15000, 10)
        print("All inputs are valid ✅")
    except ValueError as e:
        print("Input Error:", e)
