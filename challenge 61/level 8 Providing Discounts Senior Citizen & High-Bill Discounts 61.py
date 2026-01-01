# Level 8: Applying Discounts

# Step 1: Declare constants
GST_RATE = 0.18

# Step 2: Declare service costs (standalone requirement)
costs = [500, 300, 800, 1500, 4000, 7000]

# Step 3: Accept patient age
age = int(input("Enter patient age: "))

# Step 4: Accept selected service numbers
choices = input("Enter selected service numbers (comma-separated): ").split(',')

selected_costs = []

# Step 5: Fetch selected costs
for choice in choices:
    index = int(choice.strip()) - 1
    if 0 <= index < len(costs):
        selected_costs.append(costs[index])
    else:
        print("Invalid service number:", choice)

# Step 6: Calculate subtotal
subtotal = sum(selected_costs)
print(f"\nSubtotal (Before Discount): ₹{subtotal}")

# Step 7: Apply senior citizen discount
discount = 0
if age >= 60:
    senior_discount = subtotal * 0.10
    discount += senior_discount
    print(f"Senior Citizen Discount (10%): ₹{senior_discount}")

# Step 8: Apply high-bill discount (after senior discount)
discounted_subtotal = subtotal - discount
if discounted_subtotal > 5000:
    high_bill_discount = discounted_subtotal * 0.05
    discount += high_bill_discount
    print(f"High Bill Discount (5%): ₹{high_bill_discount}")

# Step 9: Final subtotal after discounts
final_subtotal = subtotal - discount
print(f"Subtotal After Discounts: ₹{final_subtotal}")

# Step 10: Apply GST
gst_amount = final_subtotal * GST_RATE
grand_total = final_subtotal + gst_amount

# Step 11: Display final bill
print(f"GST (18%): ₹{gst_amount:.2f}")
print(f"Grand Total Payable: ₹{grand_total:.2f}")
