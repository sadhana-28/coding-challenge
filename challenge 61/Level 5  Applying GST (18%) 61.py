# Level 5: Applying GST (18%)

# Step 1: Declare GST rate
GST_RATE = 0.18

# Step 2: Declare costs array
costs = [500, 300, 800, 1500, 4000, 7000]

# Step 3: Accept selected service numbers
choices = input("Enter selected service numbers (comma-separated): ").split(',')

selected_costs = []

# Step 4: Fetch selected costs
for choice in choices:
    index = int(choice.strip()) - 1
    if 0 <= index < len(costs):
        selected_costs.append(costs[index])
    else:
        print("Invalid service number:", choice)

# Step 5: Calculate subtotal
subtotal = sum(selected_costs)

# Step 6: Calculate GST and Grand Total
gst_amount = subtotal * GST_RATE
grand_total = subtotal + gst_amount

# Step 7: Display results
print("\nSubtotal (Before Tax): ₹", subtotal)
print("GST (18%): ₹{:.2f}".format(gst_amount))
print("Grand Total: ₹{:.2f}".format(grand_total))
