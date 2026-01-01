# Level 7: Admin - Setting Up Services of the Day

# Step 1: Initialize empty arrays
services = []
costs = []

# Step 2: Admin enters number of services
n = int(input("Enter number of services for today: "))

# Step 3: Read service names and costs
for i in range(n):
    service_name = input(f"Enter name of service {i + 1}: ")
    service_cost = int(input(f"Enter cost of {service_name}: "))

    # Store service name and cost in parallel arrays
    services.append(service_name)
    costs.append(service_cost)

# Step 4: Display configured services
print("\nServices Configured for Today:")
for i in range(len(services)):
    print(f"{i + 1}. {services[i]} - ₹{costs[i]}")
