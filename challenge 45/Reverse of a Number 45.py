def reverse_number(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    return reverse


if __name__ == "__main__":
    number = 12345
    result = reverse_number(number)
    print(f"Reverse of {number} is {result}")
