def create_array():
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter element {i+1}: ")))

    print("Array:", arr)


if __name__ == "__main__":
    create_array()
