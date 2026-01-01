def number_to_words(num):
    digit_words = {
        '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three',
        '4': 'Four', '5': 'Five', '6': 'Six',
        '7': 'Seven', '8': 'Eight', '9': 'Nine'
    }

    for digit in str(num):
        print(digit_words[digit], end=" ")


if __name__ == "__main__":
    number_to_words(270176)
