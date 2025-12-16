def generate_report_card(student_name, marks):
    """
    Generates a student report card with total, average, and class secured.

    Parameters:
    student_name (str): Name of the student
    marks (list): List of three subject marks

    Returns:
    dict: Report card details

    Raises:
    ValueError: If inputs are invalid
    """

    # Validate student name
    if not isinstance(student_name, str) or not student_name.strip():
        raise ValueError("Student name must be a non-empty string")

    # Validate marks
    if not isinstance(marks, list) or len(marks) != 3:
        raise ValueError("Exactly three subject marks must be provided")

    for mark in marks:
        if not isinstance(mark, (int, float)):
            raise ValueError("Marks must be numeric")
        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100")

    total = sum(marks)
    average = total / 3

    # Class determination
    if average >= 60:
        grade_class = "First Class"
    elif average >= 50:
        grade_class = "Second Class"
    elif average >= 35:
        grade_class = "Pass Class"
    else:
        grade_class = "Fail"

    return {
        "name": student_name,
        "total": total,
        "average": average,
        "class": grade_class
    }


if __name__ == "__main__":
    name = "Ananya"
    scores = [78, 65, 72]

    report = generate_report_card(name, scores)

    print("Student Report Card")
    print("-------------------")
    print(f"Name    : {report['name']}")
    print(f"Total   : {report['total']}")
    print(f"Average : {report['average']:.2f}")
    print(f"Class   : {report['class']}")
