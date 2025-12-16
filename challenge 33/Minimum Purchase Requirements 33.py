def check_minimum_purchase(total):
    if total < 500:
        print("Minimum purchase amount of ₹500 not met.")
        return

    print("Minimum purchase condition met. Invoice generated.")


if __name__ == "__main__":
    check_minimum_purchase(450)
