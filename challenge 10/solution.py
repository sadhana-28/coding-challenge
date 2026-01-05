def generate_report_card():
    # Explicit inputs
    name = input("Enter Student Name: ")

    mark1 = float(input("Enter marks for Subject 1: "))
    mark2 = float(input("Enter marks for Subject 2: "))
    mark3 = float(input("Enter marks for Subject 3: "))

    # Calculate total and average
    total = mark1 + mark2 + mark3
    average = total / 3

    # Check individual subject pass condition
    if mark1 < 35 or mark2 < 35 or mark3 < 35:
        result_class = "Fail"
    else:
        # Class determination based on average
        if average >= 60:
            result_class = "First Class"
        elif average >= 50:
            result_class = "Second Class"
        elif average >= 35:
            result_class = "Pass Class"
        else:
            result_class = "Fail"

    # Display formatted report
    print("\n--- Student Report Card ---")
    print(f"Name          : {name}")
    print(f"Total Marks  : {total:.2f}")
    print(f"Average Marks: {average:.2f}")
    print(f"Class Secured: {result_class}")


if __name__ == "__main__":
    generate_report_card()
