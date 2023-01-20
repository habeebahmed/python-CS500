# Write a Python program that will handle the checkout hotel room. 
# This hotel charges $155 for one person, $160 for two, and $165 for three or more. The tax is 12%.

# Get the number of nights and number of people in the room from the customer
# Get the meal charges from the restaurant
# Calculate bill
    # Look up the room charge for that number of people
    # Multiply by the number of nights
    # Add the meal charges
# Calculate and add the tax
# Print the bill

print("Calculating hotel bill")

# Get the number of nights and number of people in the room from the customer
number_of_nights = int(input("Please enter number of nights stayed by Customers: "))
number_of_guests = int(input("Please enter number of people stayed in the room: "))

meal_charges = int(input("Please enter meal charges incured by the customer: "))
one_day_charge = 0
tax = 0.12
# case 1 person: $155
if (number_of_guests == 1):
    one_day_charge = 155
# case 2 person: $160
elif (number_of_guests == 2):
    one_day_charge = 160
# case >=3 person: $165
else:
    one_day_charge = 165
# Total charges before tax
total_charges_before_tax = ( one_day_charge * number_of_nights ) + meal_charges
# tax 12%
tax_incured = total_charges_before_tax * tax
# Total charges
total_charges_after_tax = total_charges_before_tax + tax_incured

print("Bill Details:\n")
print("Room Charges =\t", one_day_charge)
print("Number of nights:\t{}".format(number_of_nights))
print("Meal Charges =\t${}".format(meal_charges))
print("Subtotal =\t", total_charges_before_tax)
print("Tax {}% =\t{}".format(tax*100, tax_incured))
print("Total =\t", total_charges_after_tax)
