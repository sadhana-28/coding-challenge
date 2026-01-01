# Level 2: Displaying Services & Patient Selection

# Step 1: Declare services array (MANDATORY)
services = [
    "General Consultation",
    "Blood Test",
    "Covid Test",
    "X-Ray",
    "CT Scan",
    "MRI"
]

# Step 2: Display services
print("Available Services:")
for i in range(len(services)):
    print(f"{i + 1}. {services[i]}")

# Step 3: Patient selects services
choices = input("\nEnter service numbers separated by comma: ").split(',')

selected_services = []

for choice in choices:
    index = int(choice.strip()) - 1
    if 0 <= index < len(services):
        selected_services.append(services[index])
    else:
        print("Invalid service number:", choice)

# Step 4: Display selected services
print("\nSelected Services:")
print(selected_services)
