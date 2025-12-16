# Level 3: Fetching Costs of Selected Services

# Step 1: Declare services and costs arrays
services = [
    "General Consultation",
    "Blood Test",
    "Covid Test",
    "X-Ray",
    "CT Scan",
    "MRI"
]

costs = [500, 300, 800, 1500, 4000, 7000]

# Step 2: Accept selected service numbers
choices = input("Enter selected service numbers (comma-separated): ").split(',')

selected_services = []
selected_costs = []

# Step 3: Match services with costs
for choice in choices:
    index = int(choice.strip()) - 1
    if 0 <= index < len(services):
        selected_services.append(services[index])
        selected_costs.append(costs[index])
    else:
        print("Invalid service number:", choice)

# Step 4: Display results
print("\nSelected Services:", selected_services)
print("Selected Costs   :", selected_costs)
