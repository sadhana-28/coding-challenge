def apply_payment_surcharge(total):
    method = input("Enter payment method (cash/card): ").lower()

    if method == "card":
        surcharge = total * 0.02
        total += surcharge
        print(f"Card Surcharge: ₹{surcharge:,.2f}")

    print(f"Final Payable Amount: ₹{total:,.2f}")


if __name__ == "__main__":
    apply_payment_surcharge(12000)
