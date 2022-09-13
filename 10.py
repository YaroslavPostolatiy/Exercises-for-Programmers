# №10

price_of_item1 = float(input("Enter the price of item 1:"))
quantity_of_item1 = float(input("Enter the quantity of item 1:"))
price_of_item2 = float(input("Enter the price of item 2:"))
quantity_of_item2 = float(input("Enter the quantity of item 2:"))
price_of_item3 = float(input("Enter the price of item 3:"))
quantity_of_item3 = float(input("Enter the quantity of item 3:"))

item1 = price_of_item1 * quantity_of_item1
item2 = price_of_item2 * quantity_of_item2
item3 = price_of_item3 * quantity_of_item3
subtotal = item1 + item2 + item3

print("Subtotal:", subtotal)

tax = float(subtotal * 5.5 / 100)

print("Tax:", tax)

total = float(subtotal + tax)

print("Total:", total)

# Enter the price of item 1: 25
# Enter the quantity of item 1: 2
# Enter the price of item 2: 10
# Enter the quantity of item 2: 1
# Enter the price of item 3: 4
# Enter the quantity of item 3: 1
# Subtotal: $64.00
# Tax: $3.52
# Total: $67.52
