# Level 4: Calculating Total Cost Before Tax

# Step 1: Declare costs array
costs = [500, 300, 800, 1500, 4000, 7000]

# Step 2: Accept selected service numbers
choices = input("Enter selected service numbers (comma-separated): ").split(',')

selected_costs = []

# Step 3: Fetch selected costs
for choice in choices:
    index = int(choice.strip()) - 1
    if 0 <= index < len(costs):
        selected_costs.append(costs[index])
    else:
        print("Invalid service number:", choice)

# Step 4: Calculate subtotal
subtotal = sum(selected_costs)

# Step 5: Display subtotal
print("\nSelected Costs:", selected_costs)
print(f"Total Cost (Before Tax): ₹{subtotal}")
