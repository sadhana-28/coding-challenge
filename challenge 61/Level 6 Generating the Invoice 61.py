# Level 6: Generating the Patient Invoice

# Step 1: Declare services and costs
services = [
    "General Consultation",
    "Blood Test",
    "Covid Test",
    "X-Ray",
    "CT Scan",
    "MRI"
]

costs = [500, 300, 800, 1500, 4000, 7000]
GST_RATE = 0.18

# Step 2: Collect patient details
name = input("Enter Patient Name: ")
age = int(input("Enter Age: "))
gender = input("Enter Gender: ")
contact = input("Enter Contact Number: ")

# Step 3: Display services
print("\nAvailable Services:")
for i in range(len(services)):
    print(f"{i + 1}. {services[i]}")

# Step 4: Patient selects services
choices = input("\nEnter service numbers separated by comma: ").split(',')

selected_services = []
selected_costs = []

for choice in choices:
    index = int(choice.strip()) - 1
    if 0 <= index < len(services):
        selected_services.append(services[index])
        selected_costs.append(costs[index])
    else:
        print("Invalid service number:", choice)

# Step 5: Calculate subtotal, GST, and grand total
subtotal = sum(selected_costs)
gst_amount = subtotal * GST_RATE
grand_total = subtotal + gst_amount

# Step 6: Print invoice
print("\n-----------------------------------------------")
print("HealWell Care Hospital")
print("Patient Invoice")
print("-----------------------------------------------")

print("Patient Information:")
print(f"Name   : {name}")
print(f"Age    : {age}")
print(f"Gender : {gender}")
print(f"Contact: {contact}")

print("\nServices Availed:")
for i in range(len(selected_services)):
    print(f"{i + 1}. {selected_services[i]}: ₹{selected_costs[i]}")

print(f"\nSubtotal: ₹{subtotal}")
print(f"GST (18%): ₹{gst_amount:.2f}")
print(f"Grand Total: ₹{grand_total:.2f}")

print("\nThank you for choosing HealWell Care Hospital!")
print("-----------------------------------------------")
