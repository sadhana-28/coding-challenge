def separate_whole_fraction(num):
    whole = int(num)
    fraction = num - whole

    print(f"Whole Part: {whole}")
    print(f"Fractional Part: {fraction}")


if __name__ == "__main__":
    separate_whole_fraction(123.456)
