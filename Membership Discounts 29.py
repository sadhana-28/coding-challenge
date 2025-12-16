def apply_membership_discount(total):
    member = input("Is the customer a member? (y/n): ").lower()

    if member == 'y':
        total *= 0.98

    print(f"Final Total after Membership Discount: ₹{total:,.2f}")


if __name__ == "__main__":
    apply_membership_discount(9500)
